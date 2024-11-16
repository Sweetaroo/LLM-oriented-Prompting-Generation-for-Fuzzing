from Fuzz4All.model import Phi3
import os
from Fuzz4All.target.target import INITIAL_PROMPTS
import os
import signal
import time
import openai

# This is im-prompting pipeline! Good luck!
output_folder = '/home/yrd/prompts'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

def request_gpt(prompt):
    """ Get the response of gpt4, given the prompt """
    client = openai.OpenAI(
        base_url= "https://api.gpts.vin/v1",
        api_key = "sk-5oH9yO0yROe97MKk9b317c65863a495fAdF45006E36e4a0d"
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
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
    )

    return response.choices[0].message.content

template = """
Hi. We're trying to fuzz the gcc compiler. We'll need an effective prompt to guide a LLM
to generate code snippets with high diversity.
Please follow the following instructions to generate a better, more comprehensive prompt:
1. identify what c features are described in the following two prompts:
  Prompt 1: <prompt1>
  Prompt 2: <prompt2>
2. construct a prompt that integrates the c features collected in step 1. The resulting prompt
must contain short descriptions or code examples of these c features.
3. Add some new and rare c features to the prompt and generate a final prompt bracketed with 
<prompt> and </prompt>.
"""

collection = []

def im_prompt():
    best_prompt = INITIAL_PROMPTS[0]
    for i in range(3, len(INITIAL_PROMPTS)):
        prompt = INITIAL_PROMPTS[i]
        prompt = template.replace('<prompt1>', best_prompt).replace('<prompt2>', prompt)
        response = request_gpt(prompt)
        print (response)
        collection.append(response)

import subprocess
import time

def grade_prompt(prompt, fuzz=50):
    """ criteria is line coverage """
    # load model
    mn = 'microsoft/Phi-3-mini-128k-instruct'
    model = Phi3(mn, 'cuda', [], 1300)

    # prepare output folder
    output_folder = f'/home/Fuzz4All/outputs/full_run/tmp{str(time.time())[:5]}'
    if os.path.exists(output_folder):
        os.system(f'rm -rf {output_folder}')
    os.mkdir(output_folder)
    assert os.path.exists(output_folder), "FATAL: failed to make directory"

    # generate .fuzz
    fz = 0
    for i in range(fuzz):
        ret = model.generate(prompt)
        for code in ret:
            fn = os.path.join(output_folder, f'{fz}.fuzz')
            with open(fn, 'w') as fobj:
                fobj.write(code)
            fz += 1
        del ret
        # print (fz)

    # collect line coverage
    ret = os.system(
        f"python /home/Fuzz4All/tools/coverage/C/collect_coverage.py --interval 500 --folder {output_folder}"
    )
    assert ret == 0, "FATAL: collect line cov failed"

    # read csv file
    import csv
    fn = os.path.join(output_folder, 'coverage.csv')
    last = None
    with open(fn, 'r') as fobj:
        reader = csv.reader(fobj) 
        for row in reader:
            last = row

    # clean up, avoid CUDA OUT OF MEMORY ERROR
    del model
    # os.system(f'rm -rf {output_folder}')
    return int(last[1])
