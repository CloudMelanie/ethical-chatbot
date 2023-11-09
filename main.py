from openai import OpenAI
import streamlit as st

# export OPENAI_API_KEY='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'

laptop_image = "/Users/ogunrindekirk/Downloads/CS 3373/ethical-chatbot/photos/pngtree-apple-macbook-pro-green-screen-png-image_6535120.png"

# # --- UI Configurations --- #
# st.set_page_config(page_title="Ethical ChatBot for Making Ethical Decisions",
#                    page_icon=laptop_image,
#                    layout="wide")

st.header("Ethical Chatbot")

client = OpenAI()

text = st.text_area("Write your query...")
query = st.text_input()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an Ethical Chatbot who answers questions ."},
    {"role": "user", "content": "{query}"}
  ]
)

st.write(completion.choices[0].message)