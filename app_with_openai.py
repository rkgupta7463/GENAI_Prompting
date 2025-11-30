from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key=os.getenv('GEMINI_API_KEY')

client=OpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

response=client.chat.completions.create(
    model='gemini-2.5-flash',
    messages=[
        {'role':'system','content':"You are a helpful assistent to provide the knowledge of Generative AI, Machine learning and Overall AI fields. Beyoud if you are getting any question then say sorry, it's not related to my experties!"},
        {'role':'user','content':"Hey, I'm Rishu Kumar Gupta! Nice to meet you! can you explain me how to implement the OLLAMA LLMs from hugging face?"}
    ]
)

print(response.choices[0].message.content)
