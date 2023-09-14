import streamlit as st
from streamlit_option_menu import option_menu
import pybase64
import warnings

st.set_page_config(page_title="Selvamani Andiappan",
                   page_icon="",
                   layout="wide",
                   initial_sidebar_state="expanded")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return pybase64.b64encode(data).decode()
img = get_img_as_base64("Background.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.title("Selvamani Andiappan")
