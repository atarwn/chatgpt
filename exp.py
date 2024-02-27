import os
import openai
from openai import OpenAI


client = OpenAI(
  api_key=os.environ['KEY'],
)

prompt = input("You: ")

completion = client.completions.create(
    engine="gpt-3.5-turbo",
    prompt=prompt,
    max_tokens=128,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(f"ChatGPT: {completion.choices[0].text}")
