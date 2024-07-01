import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def app():
    st.markdown("# **CHOQUE**")

    st.markdown("### Dos pelotas, una de **tenis** y una de **basquet** chocan")

    texto = """
            Durante este experimento, medimos las masas de ambas pelotas, 
            así como sus velocidades iniciales y finales. 
            Estos datos nos permitieron calcular la cantidad de movimiento (momentum) 
            antes y después del choque, y determinar si hubo pérdida de energía, calculando 
            la energía cinética antes y después del impacto.
           Los resultados obtenidos confirmaron que, por un lado, la cantidad de movimiento
           se conserva antes y después del choque, cumpliendo con el principio de conservación del momento lineal. 
           Por otro lado, el choque resultó ser inelástico, ya que se observó
           una pérdida de parte de la energía cinética, que se disipa en forma de calor, sonido u otras formas de energía no recuperables.

       """
    st.markdown(texto)

    # Link:
    # https://drive.google.com/file/d/1LeyBvFRo9xSo2VaN3w5FjhJd9ot86fbs/view?usp=drive_link
    # id video = 1LeyBvFRo9xSo2VaN3w5FjhJd9ot86fbs

    video_url = 'https://drive.google.com/file/d/1LeyBvFRo9xSo2VaN3w5FjhJd9ot86fbs/preview'

    # Insertar el video usando HTML
    st.markdown(f"""
            <div style="text-align: center;">
                 <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
             </div>
            """, unsafe_allow_html=True)


