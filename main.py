import streamlit as st
import pandas as pd
import requests

st.title("Chicago Fisicos")

url = ("https://raw.githubusercontent.com/95sv/repo_fisica/main/chewer.csv")

df = pd.read_csv(url, delimiter=',')

st.dataframe(df)

#https://drive.google.com/file/d/1RWtqI_ZqExIyvrCIzwQQmMt0qDv67mHY/view?usp=sharing

#https://drive.google.com/uc?export=download&id=1RWtqI_ZqExIyvrCIzwQQmMt0qDv67mHY

# ID del video en Google Drive
video_id = '1yRrGMfC26jI2qizgLljeAp7saDFM4Atu'

# Enlace embebido de Google Drive
video_url = 'https://drive.google.com/file/d/1yRrGMfC26jI2qizgLljeAp7saDFM4Atu/preview'

# Título de la aplicación
st.title("Video procesado chipi")

# Insertar el video usando HTML
st.markdown(f"""
    <div style="text-align: center;">
        <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
    </div>
    """, unsafe_allow_html=True)
