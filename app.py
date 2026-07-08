import pickle
import streamlit as st
from src.preprocess import cleanup

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
st.set_page_config(page_title = 'Email Spam Detection', layout= 'centered')
st.title('Email Spam Detection')

text = st.text_area('Enter your email/text :', placeholder = 'Text...')

@st.cache_resource
def load_models():
    model = load_model(BASE_DIR/'models/Spam_detection.keras')
    with open(BASE_DIR/'models/vocabulary.pkl','rb') as f :
        vocab = pickle.load(f)
        
    vectorizer = TextVectorization(
        max_tokens = 8000,
        output_sequence_length = 200
    )
    vectorizer.set_vocabulary(vocab)
    return model, vectorizer

model, vectorizer = load_models()

if st.button('predict'):
    clean_text=  cleanup(text)
    vec = vectorizer([clean_text])
    y_pred = model.predict(vec)[0][0]
    
    if y_pred>=0.5:
        st.write ("Spam")
    else :
        st.write("Ham email")
    st.write(f"Spam probability:{y_pred:.2f} ")