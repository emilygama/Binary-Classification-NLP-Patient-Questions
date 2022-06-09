import streamlit as st
from streamlit_chat import message as st_message
import time
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import requests

st.title('Online Chat Interface Example')

st.markdown("""---""")

st.write('Type a question into the chat box below. The bot will then connect you with either a general physician or a pharmacist, depending on your needs.')

st.cache()

model = pickle.load(open('rfc-pipe-model.pkl', 'rb'))

if 'history' not in st.session_state:
    st.session_state.history = []

def generate_answer():
    user_message = st.session_state.input_text
    result = model.predict([f'{user_message}'])
    message_bot = [] 
    if result == 0:
        message_bot.append('Connecting you with a general physician...')
    else:
        message_bot.append('Connecting you with a pharmacist...')
    
    next_message = []
    if result == 0:
        next_message.append('Hi! My name is Dr. Gama. I am the doctor on call to help answer your question today.')
    else:
        next_message.append('Hi! My name is Dr. Gama. I am the pharmacist on call to help answer your question today.')
        
    st.session_state.history.append({'message': user_message, 'is_user': True, 'avatar_style': 'pixel-art'})
    st.session_state.history.append({'message': message_bot, 'is_user': False})

    st.session_state.history.append({'message': next_message, 'is_user': False})

st.text_input('', key='input_text', on_change=generate_answer)

for chat in st.session_state.history:
    st_message(**chat)

st.markdown("""---""")




