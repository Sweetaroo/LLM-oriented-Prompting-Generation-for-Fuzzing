# LLM-oriented-Prompting-Generation-for-Fuzzing
A novel prompting technique that can generate and utilize multiple LLM-oriented prompts.The method explores the limit of LLM and makes LLMs generate large amounts of grammatical code with very high diversity.

# Prompts

We provide LLM-oriented prompts in [prompts](./prompts) folder.

# Usage

[main.py](./main.py): Perform LLM-oriented prompt generation.

## Synopsis
```
main.py [-h] [--output_folder OUTPUT_FOLDER] [--max-retries MAX_RETRIES] [--model_name MODEL_NAME] 
             [--max_new_tokens MAX_NEW_TOKENS]
             [--language LANGUAGE] [--feature FEATURE] [--device DEVICE]  [--api_key API_KEY]
```

## Description
The [main.py](./main.py) script performs LLM evaluation and generates prompts.

## Options
```
  -h, --help            show this help message and exit
  --output_folder OUTPUT_FOLDER
                        output folder to write resulting prompts and logs
  --max-retries MAX_RETRIES
                        maximum number of retries
  --model_name MODEL_NAME
                        model under test
  --max_new_tokens MAX_NEW_TOKENS
                        max new tokens to generate by the model
  --language LANGUAGE   targeted language
  --feature FEATURE     language feature to use as prompt
  --device DEVICE       device to run generation LLM
  --api_key API_KEY     Your openai api key
```
