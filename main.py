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
img = get_img_as_base64("bg.jpg")
sideimg = get_img_as_base64("sbg.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{sideimg}");
background-position: 100%; 
background-repeat: repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#st.markdown("<h1 style='color: BLACK;'><U>SELVAMANI ANDIAPPAN</h1>", unsafe_allow_html=True)
st.title('SELVAMANI ANDIAPPAN')

'SELVAMANI ANDIAPPAN'
'''Hope you are doing great<b>
see you soon'''

with st.sidebar:
    option_menu("Options",options=['Home','Professional','Education','Projects','Contact'],default_index=0,orientation='vertical')
