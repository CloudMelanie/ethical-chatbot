from openai import OpenAI
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# image load
client = OpenAI(
    api_key="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"
)

# title
st.title("Ethical Chatbot")
st.write("Welcome to our Ethical Chatbot Application. Enter a prompt: ")


message = st.text_input("Prompt: ", key="user_input")
st.write("You asked: ", message)

pressed = True
col1, col2, col3 = st.columns(3)

if col1.button(":green[Positive  :smile:] ", help="Provides an answer to the posed question from a positive position",
               type="primary"):
    message += "Answer from a positive point of view. Do not include the words 'positive point of view' in the response."

if col2.button(":white[Neutral  :neutral_face:]", help="Provides an answer to the posed question from a neutral position",
               type="primary"):
    message += "Answer from a neutral point of view. Do not include the words 'neutral point of view' in the response."

if col3.button(":red[Negative  :slightly_frowning_face:]", help="Provides an answer to the posed question from a negative position",
               type="primary"):
    message += "Answer from a negative point of view. Do not include the words 'negative point of view' in the response."

# Prompt user for input

if message.lower() == "quit":
    st.balloons()
    exit()

else:
    if message:
        if pressed == 0:
            message += "Answer from a neutral point of view"

        st.write("Chatbot: Thinking of a good response. Hang tight.........")
        st.write("")
        # else put the message into the gpt engine and print response
        messages = [
            {"role": "user", "content": f"{message}"}
        ]
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = completion.choices[0].message.content

        # Display the response
        st.markdown(f"Chatbot: {answer}")
        messages.append({"role": "assistant", "content": answer})


container = st.container()
container.markdown("<br>"*14, unsafe_allow_html=True)
col1, col2, col3 = container.columns(3)

# Add buttons to each column
with col2:
    if st.button("Return to Home", type="primary"):
        switch_page("Home")
