import streamlit as st
from PIL import Image


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: linear-gradient(purple,black);
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}"""


st.set_page_config(
    page_title="ZLDK",
)

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("ZLDK")

col1, col2 = st.columns(2)

with col1:
   st.header("Redbubble")
   image = Image.open('hh.jpg')
   st.image(image)
   link = '[Click here to go to Redbubble Store](https://zldk.redbubble.com)'
   st.markdown(link, unsafe_allow_html=True)

with col2:
   st.header("TeePublic")
   image = Image.open('ede61d045dfa38fe1e755e98c9153ce5.jpeg')
   st.image(image)
   link = '[Click here to go to TeePublic Store](https://www.teepublic.com/user/zldk)'
   st.markdown(link, unsafe_allow_html=True)