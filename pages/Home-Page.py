import streamlit as st

# Create a container to center the buttons
container = st.container()

container.markdown("<br>"*10, unsafe_allow_html=True)

col1, col2, col3, col4 = container.columns(4)

# Add buttons to each column
with col1:
    home_button = st.button("Home", type="primary")

with col2:
    chat_button = st.button("Chat", type="primary")

with col3:
    how_to_button = st.button("How to", type="primary")

with col4:
    about_us_button = st.button("About Us", type="primary")

container.markdown("<br>"*9, unsafe_allow_html=True)

center = st.container()
c1, c2, c3 = center.columns(3)

with c2:
    ts_button = st.button("Terms and Conditions", type="primary")

