from openai import OpenAI
from dotenv import load_dotenv
import os

#fixed api key
#client = OpenAI(api_key="sk-xxxx")

#load .env key
load_dotenv()
client = OpenAI(api_key=os.getenv('openapi_key'))

def chat_with_gpt(prompt):
	response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages=[
        {"role": "user", "content": prompt}
    ]
)
	
	return response.choices[0].message.content.strip()


if __name__ == "__main__":
	while True:
		user_input = input("You: ")
		if user_input.lower() in ["quit", "exit", "q", "bye"]:
			break
		response= chat_with_gpt(user_input)
		print(f"Chatbot: {response}")