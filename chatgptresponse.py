import openai
import re

def responseprompt(prompt):

    openai.api_key = "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"

    model_engine = "text-davinci-003"
    prompt = prompt

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response

def preprocessedresponse(prompt):
    res = responseprompt(prompt)
    inslist = []
    totlist = []
    c = -1
    str1 = 'Instructions:'
    for i in range(0, len(res.split("\n"))):
        totlist.append(res.split("\n")[i])
    totlist = list(filter(lambda x: x.strip(), totlist))
    start_index = totlist.index("Instructions:") + 1
    inslist = totlist[start_index:]
    inslist = [re.sub(r'^\d+', '', string) for string in inslist]
    inslist = [string.lstrip(" .") for string in inslist]
    inslist = [string.rstrip(". ") for string in inslist]
    return inslist

# print(preprocessedresponse("How to make Potato Cauliflower Recipe?"))