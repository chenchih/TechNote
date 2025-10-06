from openai import OpenAI
from dotenv import load_dotenv()
import os

#fixed api key
#client = OpenAI(api_key="sk-xxxx")

#load .env key
load_dotenv()
client = OpenAI(api_key=os.getenv('openapi_key'))


def test_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",    
        max_tokens=20,            # limit response length
        messages=[
            {"role": "system", "content": "hello chatgpt."},
            {"role": "user", "content": "Write a hello world code"}
        ]
    )
    
    #print(completion.choices[0].message.content)
    return completion.choices[0].message.content

if __name__ == "__main__":
    response= test_gpt("hello")
	print("Chatbot": response)

#note:
#system: Defines the rules of the conversation, make instructions fixed and persistent across the whole conversation. if not set as sytem , you have to write every time
#ex:{"role": "system", "content": "You are a strict English teacher."}
#user: Represents what the person actually asked.
#reference:https://www.youtube.com/watch?v=CHsRy4gl6hk