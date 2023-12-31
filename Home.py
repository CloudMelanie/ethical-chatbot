import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header 


def header():
    colored_header(
        label="Welcome to the Ethics Chatbot",
        description= "",
        color_name="violet-70",
    )
header()

imageHome = "photos/ethics_image.png"
st.image(imageHome)


# Create a container to center the buttons
container = st.container()

container.markdown("<br>"*2, unsafe_allow_html=True)

col1, col2, col3, col4 = container.columns(4)

# Add buttons to each column
with col1:
    if st.button("Home", type="primary"):
        switch_page("Home")
with col2:
    if st.button("Chat", type="primary"):
        switch_page("Chat")
with col3:
    if st.button("How to", type="primary"):
        switch_page("How to Use")
with col4:
    if st.button("About Us", type="primary"):
        switch_page("About Us")

container.markdown("<br>"*4, unsafe_allow_html=True)

center = st.container()
c1, c2, c3 = center.columns(3)

with c2:
    if st.button("Terms and Conditions", type="primary"):
        switch_page("Terms and Conditions")
