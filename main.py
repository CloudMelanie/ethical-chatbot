from openai import OpenAI
import streamlit as st

# export OPENAI_API_KEY='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'

st.title("Ethical ChatBot for Making Ethical Decisions")

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Should the government have access to all my information?"}
  ]
)

print(completion.choices[0].message)