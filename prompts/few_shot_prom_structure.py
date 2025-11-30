from openai import OpenAI
from dotenv import load_dotenv
import os

'''
1. Few-shot prompting: Directly giving the inst to model and few examples to the model. 
Additionally, we can structure the output response as expected format. 
'''

load_dotenv()

gemini_api_key=os.getenv('GEMINI_API_KEY')

client=OpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

SYSTEM_PROMPT="""
You should only and only ans the coding related questions. Do not ans anything else. Your name is Gemini. If user asks something else other than coding, just say sorry, i can't answer it.

RULE:
- Strictly follow the output in JSON format

Output Format:
{{
    "code":"string" or null,
    "IscodingQution":boolean,
    "message": Sorry, I can only help with coding related questions.
}}


Example 
Q: Can you explain the a + b whole square?
A: {{
    "code":null,
    "IscodingQution": false,
    "message": Sorry, I can only help with coding related questions.
}}

Q: Hey, write the python code to sumation of two number?
A: 
{{
    "code":"
            def add(a,b):
                return  a+b",
    "IscodingQution":true,
    "message": Here it is coding.
}}


"""

response=client.chat.completions.create(
    model='gemini-2.5-flash',
    messages=[
        {'role':'system','content':SYSTEM_PROMPT},
        {'role':'user','content':"Hey, I'm Rishu Kumar Gupta! how to set up the celery in django in window?"}
    ]
)

print(response.choices[0].message.content)

