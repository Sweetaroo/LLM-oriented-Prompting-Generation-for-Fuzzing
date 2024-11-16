import os
os.environ["CUDA_VISIBLE_DEVICES"]="2"
from typing import Any, Dict, List, Optional, Tuple, Union

import torch
from torch.nn import DataParallel
from torch.nn.parallel import DistributedDataParallel
from torch.distributed import init_process_group
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    StoppingCriteria,
    StoppingCriteriaList,
)
from syncode import Grammar, SyncodeLogitsProcessor, Syncode

os.environ["TOKENIZERS_PARALLELISM"] = "false"  # disable warning
EOF_STRINGS = ["<|endoftext|>", "###"]


class EndOfFunctionCriteria(StoppingCriteria):
    def __init__(self, start_length, eos, tokenizer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_length = start_length
        self.eos = eos
        self.tokenizer = tokenizer
        self.end_length = {}

    def __call__(self, input_ids, scores, **kwargs):
        """Returns true if all generated sequences contain any of the end-of-function strings."""
        decoded_generations = self.tokenizer.batch_decode(
            input_ids[:, self.start_length :]
        )
        done = []
        for index, decoded_generation in enumerate(decoded_generations):
            finished = any(
                [stop_string in decoded_generation for stop_string in self.eos]
            )
            if (
                finished and index not in self.end_length
            ):  # ensures first time we see it
                for stop_string in self.eos:
                    if stop_string in decoded_generation:
                        self.end_length[index] = len(
                            input_ids[
                                index,  # get length of actual generation
                                self.start_length : -len(
                                    self.tokenizer.encode(
                                        stop_string,
                                        add_special_tokens=False,
                                        return_tensors="pt",
                                    )[0]
                                ),
                            ]
                        )
            done.append(finished)
        return all(done)

class LLMTest:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint, trust_remote_code=True,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint, trust_remote_code=True,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        self.eos = []
        self.max_length = max_length
        self.prefix_token = ""
        self.suffix_token = ""
        self.skip_special_tokens = False

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        # link: <https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base>
        input_str = self.prefix_token + prompt + self.suffix_token
        discard = """
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )
        """
        input_tokens = self.tokenizer(input_str, return_tensors="pt").cuda()

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        discard = """
        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        """
        raw_outputs = self.model.generate(
            **input_tokens, 
            max_length =min(self.max_length, len(input_tokens[0]) + max_length), 
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index])
        return outputs

def clean_markdown(code):
    start = None
    try:
        start = code.index('```c')
    except Exception:
        pass
    if start is None:
        try:
            start = code.index ('```C')
        except Exception:
            pass
    if start is None:
        return code
    code = code[start + 4:]
    try:
        end = code.index('```')
    except Exception: # not found
        return code
    return code[: end]

class Phi3:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint, trust_remote_code=True,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint, trust_remote_code=True,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        self.eos = ["<|end|>"]
        self.max_length = max_length
        self.prefix_token = "<|system|> You're a helpful programming assistant. <|end|><|user|>"
        self.suffix_token = "<|end|><|assistant|>"
        self.skip_special_tokens = False

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        input_str = self.prefix_token + prompt + self.suffix_token
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index])
        
        # unwrap ```c and ```
        for i in range(len(outputs)):
            outputs[i] = clean_markdown(outputs[i])
        return outputs

class StarCoder:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint, trust_remote_code=True,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint, trust_remote_code=True,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        self.eos = EOF_STRINGS + eos
        self.max_length = max_length
        self.prefix_token = "<fim_prefix>"
        self.suffix_token = "<fim_suffix><fim_middle>"
        self.skip_special_tokens = False

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        input_str = self.prefix_token + prompt + self.suffix_token
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index])
        return outputs

class DeepSeekCoder:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint, trust_remote_code=True,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint, trust_remote_code=True,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        self.eos = ["<｜end▁of▁sentence｜>"]
        self.max_length = max_length
        self.prefix_token = "" # "<fim_prefix>"
        self.suffix_token = "" # "<fim_suffix><fim_middle>"
        self.skip_special_tokens = True

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        input_str = self.prefix_token + prompt + self.suffix_token
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            # top_p=1.0,
            # temperature=max(temperature, 1e-2),
            top_k=50, 
            top_p=0.95,
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index])
        # for i in range (len(outputs)):
        #     outputs[i] = clean_markdown(outputs[i])
        return outputs

class StarCoderSyncode:
    """integrate syncode module into starcoder"""
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int,
        grammar: str = '/home/yrd/c_grammar.lark',  # grammar script or language name
        mode: str = 'grammar_strict' # Literal["original", "grammar_mask", "grammar_strict"]
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint,
                trust_remote_code=True,
            )
            .to(torch.bfloat16)
            .to(device)
        )

        self.eos = EOF_STRINGS + eos
        self.max_length = max_length
        self.prefix_token = "<fim_prefix>"
        self.suffix_token = "<fim_suffix><fim_middle>"
        self.skip_special_tokens = False

        # check the existence of grammar
        if grammar.endswith('.lark'):
            assert os.path.exists(grammar)
        self.grammar = Grammar(grammar)
        self.mode = mode
        # use logits processor, as in </home/yrd/eg1.py>
        self.logits_processor = SyncodeLogitsProcessor(
            grammar=self.grammar,
            tokenizer=self.tokenizer,
            parse_output_only=True,
            mode=self.mode,
        )

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:

        # reset prompt
        self.logits_processor.reset(prompt)
        input_str = self.prefix_token + prompt + self.suffix_token
        input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
            self.device
        )

        scores = StoppingCriteriaList(
            [
                EndOfFunctionCriteria(
                    start_length=len(input_tokens[0]),
                    eos=self.eos,
                    tokenizer=self.tokenizer,
                )
            ]
        )

        raw_outputs = self.model.generate(
            input_tokens,
            max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            pad_token_id=self.tokenizer.eos_token_id,
            # add grammar constraits
            logits_processor=[self.logits_processor],
        )
        gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        gen_strs = self.tokenizer.batch_decode(
            gen_seqs, skip_special_tokens=self.skip_special_tokens
        )
        outputs = []
        # removes eos tokens.
        for output in gen_strs:
            min_index = 10000
            for eos in self.eos:
                if eos in output:
                    min_index = min(min_index, output.index(eos))
            outputs.append(output[:min_index]) 
        return outputs

class CodeQwen:
    def __init__(
        self, model_name: str, device: str, eos: List, max_length: int
    ) -> None:
        checkpoint = model_name
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(
            checkpoint,
        )
        self.model = (
            AutoModelForCausalLM.from_pretrained(
                checkpoint,
            )
            .to(torch.bfloat16)
            .to(device)
        )
        # self.eos = EOF_STRINGS + eos
        self.max_length = max_length
        # self.prefix_token = "<fim_prefix>"
        # self.suffix_token = "<fim_suffix><fim_middle>"
        # self.skip_special_tokens = False
        self.skip_special_tokens = True

    @torch.inference_mode()
    def generate(
        self, prompt, batch_size=10, temperature=1.0, max_length=512
    ) -> List[str]:
        # input_str = self.prefix_token + prompt + self.suffix_token
        # input_str = prompt
        # input_tokens = self.tokenizer.encode(input_str, return_tensors="pt").to(
        #     self.device
        # )
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        model_inputs = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
        # input_tokens = model_inputs.input_ids
        # generated_ids = model.generate(
        #     model_inputs.input_ids,
        #     max_new_tokens=512
        # )
        

        
        # scores = StoppingCriteriaList(
        #     [
        #         EndOfFunctionCriteria(
        #             start_length=len(input_tokens[0]),
        #             eos=self.eos,
        #             tokenizer=self.tokenizer,
        #         )
        #     ]
        # )

        generated_ids_batch = self.model.generate(
            # model_inputs.input_ids,
            model_inputs,
            max_new_tokens=512,
            # max_length=min(self.max_length, len(input_tokens[0]) + max_length),
            do_sample=True,
            top_p=1.0,
            temperature=max(temperature, 1e-2),
            num_return_sequences=batch_size,
            # stopping_criteria=scores,
            output_scores=True,
            return_dict_in_generate=True,
            repetition_penalty=1.0,
            # pad_token_id=self.tokenizer.eos_token_id,
        )
        # generated_ids = [
        #     output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids_batch)
        # ]
        # generated_ids_batch = generated_ids_batch[:, model_inputs.input_ids.shape[1]:]
        generated_code = generated_ids_batch.sequences[:, len(model_inputs[0]):]
        # print(type(generated_ids))
        outputs = self.tokenizer.batch_decode(
            generated_code, skip_special_tokens=True
        )
        # gen_seqs = raw_outputs.sequences[:, len(input_tokens[0]) :]
        # gen_strs = self.tokenizer.batch_decode(
        #     gen_seqs, skip_special_tokens=self.skip_special_tokens
        # )
        # outputs = []
        # # removes eos tokens.
        # for output in gen_strs:
        #     min_index = 10000
        #     for eos in self.eos:
        #         if eos in output:
        #             min_index = min(min_index, output.index(eos))
        #     outputs.append(output[:min_index])
        for i in range(len(outputs)):
            outputs[i] = clean_markdown(outputs[i]) 
        return outputs

def make_model(eos: List, model_name: str, device: str, max_length: int):
    """Returns a llm model instance (optional: using the configuration file)."""

    kwargs_for_model = {
        "model_name": model_name,
        "eos": eos,
        "device": device,
        "max_length": max_length,
    }

    # print the model config
    print("=== Model Config ===")
    print(f"model_name: {model_name}")
    for k, v in kwargs_for_model.items():
        print(f"{k}: {v}")

    if "starcoder" in model_name.lower():
        model_obj = Phi3(**kwargs_for_model)
    else:
        # default
        model_obj = Phi3(**kwargs_for_model)

    model_obj_class_name = model_obj.__class__.__name__

    print(f"model_obj (class name): {model_obj_class_name}")
    print("====================")

    return model_obj
