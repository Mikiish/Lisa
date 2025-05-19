import requests
import openai

from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)

