import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("How to Use")

st.subheader("1. Enter an ethical related question.")
st.subheader("2. Select one of three stances: Positive, Neutral, or Negative.")
container = st.container()
container.markdown("<br>"*18, unsafe_allow_html=True)

col1, col2, col3 = container.columns(3)

# Add buttons to each column
with col1:
    if st.button("Click here to start!", type ="primary"):
        switch_page("Chat")
with col2:
    if st.button("return to Home", type="primary"):
        switch_page("Home")

