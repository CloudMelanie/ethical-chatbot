#from openai import OpenAI
import openai
import streamlit as st
import os

# export OPENAI_API_KEY='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'
openai.api_key= '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'
# image load
image = "C:/Users/melan/OneDrive/Documents/download.jpeg"

# displaying the image on streamlit app
st.image(image)

# title
st.title("Ethical Chatbot")
st.write("Welcome to our Ethical Chatbot Application. Enter a prompt: ")

# Prompt user for input
message = st.text_input("User: ", key="user_input")
st.write("You asked: ", message)

# Exit program if user inputs "quit"
if message.lower() == "quit":
  st.balloons()

else:
  
  if message: 
    
    # else put the message into the gpt engine and print response
    ##client = OpenAI()

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{message}"}
        ]
    )

    answer = completion.choices[0].message

    st.write("Chatbot: Thinking of a good response. Hang tight.........")
    st.write("")
    
    # Display the response
    st.markdown(f"Chatbot: {answer}")
