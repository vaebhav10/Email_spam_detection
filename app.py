import streamlit as st 
from src.predict import predict

st.set_page_config(page_title = 'Email Spam Detection', layout= 'centered')
st.title('Email Spam Detection')

text = st.text_area('Enter your email/text :', placeholder = 'Text...')
if st.button('predict'):
    if text.strip():
        st.write('Verdict : ',predict(text))
    else :
        st.write("Enter a vaild email")