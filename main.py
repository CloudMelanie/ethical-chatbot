# from openai import OpenAI
import openai
import streamlit as st
import os


# export OPENAI_API_KEY='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'
openai.api_key = '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'
# image load
image = "C:/Users/melan/OneDrive/Documents/download.jpeg"

# displaying the image on streamlit app
st.image(image)

# title
st.title("Ethical Chatbot")
st.write("Welcome to our Ethical Chatbot Application. Enter a prompt: ")


message = st.text_input("User: ", key="user_input")
st.write("You asked: ", message)



if st.button("Positive", help="Provides an answer to the posed question from a positive position",
             type="primary"):
    st.write("Positive: ")
    message += "Answer from a positive point of view"

elif st.button("Negative", help="Provides an answer to the posed question from a negative position",
           type="primary"):
    st.write("Negative")
    message += "Answer from a negative point of view"

elif st.button("Neutral", help="Provides an answer to the posed question from a neutral position",
            type="primary"):
    st.write("Neutral")
    message += "Answer from a neutral point of view"
# Prompt user for input

if message.lower() == "quit":
    st.balloons()
    exit()

else:
    if message:
        st.write("Chatbot: Thinking of a good response. Hang tight.........")
        st.write("")
        # else put the message into the gpt engine and print response
        messages = [
            {"role": "user", "content": f"{message}"}
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = completion.choices[0].message.content

        # Display the response
        st.markdown(f"Chatbot: {answer}")
        messages.append({"role": "assistant", "content": answer})
