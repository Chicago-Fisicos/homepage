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

    texto2="""
    Cualquier cosa que esté en movimiento posee energía cinética.\n
    En el **Sistema Internacional (SI)**, la unidad de energía cinética es el **Joule (J)**, la misma que la del trabajo. 
    Un **Joule** corresponde a:
    """
    st.markdown(texto2)

    # Ecuación en LaTeX
    latex_ec = r"""
    1 \, \text{kg} \cdot \text{m}^2 / \text{s}^2
    """

    # Mostrar la ecuación en Streamlit
    st.latex(latex_ec)

    st.markdown("La fórmula para calcular la energía cinética es:\n")

    latex_ec2=r"""
        \mathbf{E_c}\ = \frac{1}{2} \cdot m \cdot V^2
    """
    st.latex(latex_ec2)

    st.markdown("La energía potencial es el tipo de energía asociada a la posición relativa dentro de un sistema, "
                "es decir, la posición de un objeto con respecto a otro.\n"
                "La energía potencial elástica es la energía almacenada que resulta de aplicar una fuerza "
                "para deformar un objeto elástico."
                "Esta energía queda almacenada hasta que se elimina la fuerza y"
                " el objeto elástico regresa a su forma original, realizando trabajo en el proceso.")

    st.write("\n\n")
    # Link :
    # https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/energia_mecanica.png?raw=true

    grafico_energia = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/energia_mecanica.png?raw=true'

    # Solicitar la imagen desde la URL
    response = requests.get(grafico_energia)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Energia', use_column_width=True)

    st.markdown("## Materiales y métodos")

    texto3="""
        Para este experimento, grabamos un video en una cancha de básquet.\n
        Requerimos un trípode, un celular, una cinta métrica, una pelota de básquet y una persona.
        Realizamos tiros al aro, tomando las medidas correspondientes en el Sistema Internacional (SI) o MKS:\n
        **metro (m)**, **kilogramo (kg)** y **segundo (s)**.
        Utilizamos una balanza para pesar la pelota de básquet, obteniendo una masa de **0.62 kg**. \n
        Con la cinta métrica, medimos la altura del aro, obteniendo un resultado de **3.05 m.**
    """
    st.markdown(texto3)

    st.markdown("# INGRESAR TABLA ")

    st.markdown("## Calculos y resultados")

    texto_calculo="""
        Para calcular la energía mecánica utilizaremos las siguientes fórmulas:
    """
    st.markdown(texto_calculo)

    latex_ec3=r"""
        \mathbf{E_{MC}} \ = \mathbf{E_C} + \mathbf{E_P}
    """
    st.latex(latex_ec3)
    st.latex(latex_ec2)

    latex_ec4=r"""
        \mathbf{E_{P}} \ = \text{m} \cdot \text{g} \cdot \text{h}
    """
    st.latex(latex_ec4)

    texto4="""
        **Datos:**\n
        - Altura del aro: 3.05m
        - Masa de la pelota: 0.62kg
        - Altura de la pelota (desde donde arranca el trackeo): 2.50m
    """
    st.markdown(texto4)