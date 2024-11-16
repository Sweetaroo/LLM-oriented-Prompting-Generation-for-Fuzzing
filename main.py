import openai
import os
from Baseline.Fuzz4All.model import Phi3, CodeQwen, DeepSeekCoder
import random
import argparse 

"""
Script for performing LLM-oriented prompting. 
"""

# Global constants
lang_tag = "<lang>"
ctag = "<feature>"
ltag, rtag = "<prompt>", "</prompt>"

INSTRUCTION = f"""
#### Your Task
Please create a short {lang_tag} program that uses {ctag} in a complex way.
"""

des_template = f"""
Please briefly describe the usage of {ctag} in {lang_tag} programming language. Remember, you must also 
provide a short code example of {ctag}.
"""

# template for prompt mutation
mut_template = f"""
Please follow the following steps to generate a better, more comprehensive prompts.
1. Examine whether there's any mistake in the description of the following prompt, if so, correct it:
   Prompt: <prompt1>
2. identify what c feature is described in the prompt collected in step 1.
3. Create a concise prompt of the c feature collected in step 2. Remember, this prompt must contain a brief 
description of that c feature as well as a short code example.
4. Generate a final prompt bracketed with {ltag} and {rtag}.
"""

def make_model(args):
    device = args.device 
    eos = []
    max_token = args.max_new_tokens
    mn = args.model_name

    if 'Phi-3' in mn:
        return Phi3(mn, device, eos, max_token);
    if 'CodeQwen' in mn:
        return CodeQwen(mn, device, eos, max_token);
    if 'deepseek-coder' in mn:
        return DeepSeekCoder(mn, device, eos, max_token)
    
    assert False, f"huggingface model for {mn} is not implemented"

def parse_args():
    parser = argparse.ArgumentParser(description="prompting args.")
    parser.add_argument(
        "--output_folder", 
        type=str, 
        default='/home/prompts/', 
        help="output folder to write resulting prompts and logs"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help='maximum number of retries'
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default = "microsoft/Phi-3-mini-128k-instruct",
        help="model under test",
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=1024,
        help="max new tokens to generate by the model",
    )
    parser.add_argument(
        "--language",
        type=str,
        default='c',
        help="targeted language"
    )
    parser.add_argument(
        "--feature",
        type=str,
        default="x macros",
        help="language feature to use as prompt",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        help="device to run generation LLM",
    )
    parser.add_argument(
        "--api_key",
        type=str,
        help="Your openai api key",
    )

    return parser.parse_args()

def request_gpt_try(prompt, key):
    """ Try getting the response of gpt4, given the prompt """
    client = openai.OpenAI(
        api_key = key,
    )
    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful AI agent',
            },
            {
                'role': 'user',
                'content': prompt,
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
    )

    return response.choices[0].message.content

def request_gpt(prompt, key: str):
    """ Returns the response from LLM4 """
    res = ''
    while True:
        try:
            res = request_gpt_try(prompt, key)
        except Exception:
            pass
        finally:
            return res

def grade_prompt(prompt):
    ret = model.generate(prompt)
    i = 0
    output_folder = f'/tmp/tmp{random.randint(0, 999)}'
    if os.path.exists(output_folder):
        os.system(f'rm -rf {output_folder}')
    os.mkdir(output_folder)

    for code in ret:
        with open(os.path.join(output_folder, f'{i}.fuzz'), 'w') as fobj:
            fobj.write(code)
        i += 1

    ok = 0
    for i in range(10):
        fn = os.path.join(output_folder, f'{i}.fuzz')
        ret = os.system(f'/usr/bin/gcc -std=c2x -x c {fn}')
        if ret == 0:
            ok += 1

    return ok >= 3

def log(message, title):
    """ print logging """
    pass
    #print('=' * 32, title, '=' * 32)
    #print(message)
    #print('=' * (66 + len(title)))
    #print('')

def write_file(of, fn, fo):
    with open(os.path.join(of, fn), 'w') as fobj:
        fobj.write(str(fo))
    
def unwrap_pt(pt):
    return pt[pt.index(ltag) + len(ltag) : pt.index(rtag)]

if __name__ == '__main__':
    args = parse_args()
    log(args, 'Setup')
    model = make_model(args)

    # start prompting...
    lang = args.language
    feature = args.feature
    of = args.output_folder

    # check output folder
    if os.path.exists(of):
        log("output folder already exists! Press <enter> to continue...", "WARNING")
        _ = input()
    else:
        os.path.mkdir(of)

    # construct initial prompt, dump to file and test...
    pt_gpt = des_template.replace(lang_tag, lang).replace(ctag, feature)
    log(pt_gpt, "Prompt to GPT-4")
    response = request_gpt(pt_gpt, args.api_key)
    log(response, "GPT-4's response");
    response = response + INSTRUCTION.replace(lang_tag, lang).replace(ctag, feature)
    write_file(of, 'init-prompt.md', response)

    if grade_prompt(response):
        pass
    else:
        # try mutating the prompt...
        for i in range(args.max_retries):
            pt_gpt = mut_template.replace('<prompt1>', response)
            log(pt_gpt, "Prompt to GPT-4")
            response = request_gpt(pt_gpt, args.api_key)
            log(response, "GPT-4's response")
            write_file(of, f'retry-{i}.md', response)

            if grade_prompt(response):
                break
