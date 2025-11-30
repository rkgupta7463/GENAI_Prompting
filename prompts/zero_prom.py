from openai import OpenAI
from dotenv import load_dotenv
import os

'''
1. Zero-shot prompting: The model is given a direct question or task without prior examples. 
'''

load_dotenv()

gemini_api_key=os.getenv('GEMINI_API_KEY')

client=OpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)
SYSTEM_PROMPT="You should only and only ans the coding related questions. Do not ans anything else. Your name is Gemini. If user asks something else other than coding, just say sorry, i can't answer it."
response=client.chat.completions.create(
    model='gemini-2.5-flash',
    messages=[
        {'role':'system','content':SYSTEM_PROMPT},
        {'role':'user','content':"Hey, I'm Rishu Kumar Gupta! what is (a+b)2 ?"}
    ]
)

print(response.choices[0].message.content)

