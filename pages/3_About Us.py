import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("About Us")


# image load
logo = "photos/group4.png"
st.image(logo)

st.subheader("Who We Are")
use_text = """
        We are a group of computer science students who want to explore what Ethical Decision making looks like for us as we go into the real world.
        """
st.write(use_text)
st.write("")



# image load
image1 = "photos/IMG_3FA029931518-1.jpeg"
st.image(image1)

st.subheader("Briana")



image2 = "photos/IMG_3265.jpeg"
st.image(image2)

st.subheader("Kirk")



image3 = "photos/IMG_3285.jpeg"
st.image(image3)

st.subheader("Melanie")



image4 = "photos/IMG_7110_Original.jpg"
st.image(image4)

st.subheader("Laila")

container = st.container()
col1, col2, col3 = container.columns(3)

# Add buttons to each column
with col2:
    if st.button("return to Home", type="primary"):
        switch_page("Home")


