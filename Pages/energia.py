import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def app():
    st.markdown("# **ENERGIA**")

    st.write("\n\n")

    texto = """
        Para el estudio de la energía, realizamos un experimento en el cual grabamos un  video donde se lanza una pelota de básquet al aro. 
        Sabemos que la energía mecánica de un sistema en un momento determinado es la suma de la energía cinética,
         la energía potencial gravitatoria y la energía potencial elástica que el sistema tiene en ese momento.\n
    A través del análisis de la energía, sabemos que cuando un objeto experimenta 
    un cambio en su velocidad, su energía cinética cambia. Al analizar el movimiento 
    de la pelota de básquet, pudimos determinar su velocidad final al conocer su energía cinética.\n
    Los resultados obtenidos confirman que la relación teórica entre la energía mecánica y la velocidad final se mantiene consistente con las leyes de la física, específicamente con los principios de conservación de la energía.
    """
    st.markdown(texto)
    st.write("\n\n")
    st.markdown("## **Introduccion**")

    # Texto explicativo con la ecuación en LaTeX
    texto_energia_mecanica = """
    La energía mecánica de un sistema en un momento determinado es la suma de la energía cinética, la energía potencial y la energía elástica que el sistema tiene en ese momento. Matemáticamente, se puede expresar como:
    """

    # Explicación de los términos
    texto_explicacion = """
    donde:
    - \\( E_m \\) es la energía mecánica total,
    - \\( E_k \\) es la energía cinética,
    - \\( E_p \\) es la energía potencial,
    - \\( E_e \\) es la energía elástica.
    
    La diferencia entre energía cinética y energía potencial gravitatoria es que la primera se corresponde con los objetos en movimiento, mientras que la segunda es igual al trabajo que la fuerza peso puede realizar si se deja caer el cuerpo desde una determinada altura.

    """
    # Mostrar el texto y la ecuación en Streamlit
    st.markdown(texto_energia_mecanica)

    # Mostrar la ecuación en LaTeX
    st.latex(r"""
       E_m = E_k + E_p + E_e
       """)

    # Mostrar la explicación de los términos en Streamlit
    st.markdown(texto_explicacion)

    # Link :
    # https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/energia_mecanica.png?raw=true

    grafico_energia = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/energia_mecanica.png?raw=true'

    # Solicitar la imagen desde la URL
    response = requests.get(grafico_energia)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Energia', use_column_width=True)