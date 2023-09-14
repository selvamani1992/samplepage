import streamlit as st
from PIL import Image


st.set_page_config(page_title="Selvamani Andiappan",
                   page_icon="",
                   layout="wide",
                   initial_sidebar_state="expanded")

# Define the CSS style
background_style = """
<style>
body {
    background-image: url('Background.png');
    background-size: cover;
}
</style>
"""

# Display the CSS style using st.markdown
st.markdown(background_style, unsafe_allow_html=True)

st.title("Selvamani Andiappan")
st.title("Welcome to My Webpage")
st.image('sample.jpg')
st.write('Thank You')
