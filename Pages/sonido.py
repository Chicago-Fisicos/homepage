import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def app():
    st.markdown("# **AUDIO**")

    #LINK AUDIO:
    #   https://drive.google.com/file/d/1CczDtTo53xOFARmVvCf5P49mQDQipNFF/view?usp=drive_link

    audio_file = '1CczDtTo53xOFARmVvCf5P49mQDQipNFF'

    # Construir la URL de descarga directa
    url = f"https://drive.google.com/uc?export=download&id={audio_file}"

    url2 = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/videos-y-audios/output_with_audio.mp4?raw=true'

    # Mostrar el reproductor de audio en Streamlit
    st.audio(url2)

    # Grafico de sonido:
    # https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/graficos/grafico_picos.png

    graf_audio=' https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/graficos/grafico_picos.png?raw=true'
    # Solicitar la imagen desde la URL
    response = requests.get(graf_audio)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Picos sonido', use_column_width=True)
