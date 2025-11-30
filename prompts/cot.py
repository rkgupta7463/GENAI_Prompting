# Chain Of Thought Prompting
from openai import OpenAI,RateLimitError, APIError
from dotenv import load_dotenv
import os
import json
import time


'''
1. Zero-shot prompting: The model is given a direct question or task without prior examples. 
'''

load_dotenv()

gemini_api_key=os.getenv('GEMINI_API_KEY')

client=OpenAI(
    api_key=gemini_api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)

SYSTEM_PROMPT="""
                You're an expert AI Assistant in resolving user queries using chain of thought.
                You work on START, PLAN and OUTPUT steps.
                You need to first PLAN what needs to be done. The PLAN can be multiple steps.
                Once you think enough PLAN has been done, finally you can give an OUTPUT.

                RULE:
                    - Strickly follow the follow the json output format
                    - Only run one step at a time.
                    - The sequance of step is START (where user give an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to displayed to the user.)

                OUTPUT JSON Format:
                    {{
                        "step":"START" | "PLAN" | "OUTPUT" "content":"string"
                    }}     

                    Example:
                    Q: Hey,, can you solve 2+3*5/10
                    START: Hey, Can you solve 2 + 3 * 5 / 10
                    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
                    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
                    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
                    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
                    PLAN: { "step": "PLAN": "content": "Now the new equation is 2+ 15 / 10" }
                    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5" }
                    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
                    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
                    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
                    OUTPUT: { "step": "OUTPUT": "content": "Great, Finally output is: 3.5 }
            """

print("\n\n")

message_history=[{"role":"system","content":SYSTEM_PROMPT},]

user_query=input("Ask an question➡️:\t")
message_history.append({"role":"user","content":user_query})

while True:
    try:
        # Call the model
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=message_history
        )

        raw_result = response.choices[0].message.content

        # Append assistant message to history
        message_history.append({"role": "assistant", "content": raw_result})

        # Parse JSON safely
        try:
            parsed_result = json.loads(raw_result)
        except json.JSONDecodeError:
            print("⚠️ Model returned invalid JSON, skipping…")
            continue

        step = parsed_result.get("step")
        content = parsed_result.get("content", "")

        if step == "START":
            print("🔥", content)
            continue

        elif step == "PLAN":
            print("🧠", content)
            continue

        elif step == "OUTPUT":
            print("🤖", content)
            break

        else:
            print("⚠️ Unknown step:", step)

    except RateLimitError as e:
        print("⏳ Rate limit hit. Waiting 40 seconds...")
        time.sleep(40)
        continue

    except APIError as e:
        print("❌ API Error:", e)
        break


print("\n\n")


