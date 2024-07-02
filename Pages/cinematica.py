import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

chipi_trackeo_original = ("https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-original.csv")
chipi_trackeo_nuevo_origen = ("https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-original-nuevo-origen.csv")
chipi_curvefit = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/curve_fit.png?raw=true'
chipi_tabla_curvefit= 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-suavizado-curve-fit-nuevo-origen.csv'
grafico_posxy='https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/posicion_xy.png?raw=true'
grafico_velocidad='https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/velocidad_tiempo_X.png?raw=true'
grafico_velocidad_y='https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/velocidad_tiempo_Y.png?raw=true'
grafico_aceleracion='https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/aceleracion_tiempo_Y.png?raw=true'
rebote_tablero_curvefit = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/descartado/basket-rebote-tablero/graficos/curve_fit.png?raw=true'
rebote_tabla_nuevo_origen = 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/descartado/basket-rebote-tablero/tablas/trackeo-original-nuevo-origen.csv'
rebote_tabla_curvefit = 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/descartado/basket-rebote-tablero/tablas/trackeo-suavizado-curve-fit-nuevo-origen.csv'

data_chipi = pd.read_csv(chipi_trackeo_original, delimiter=',')
data_chipi_nuevo_origen = pd.read_csv(chipi_trackeo_nuevo_origen,delimiter =',')
data_chipi_curvefit = pd.read_csv(chipi_tabla_curvefit,delimiter =',')

data_rebote_tablero_curvefit = pd.read_csv(rebote_tabla_curvefit, delimiter =',')

fran_triple_tiro = "https://drive.google.com/file/d/1K0tGucwHLtEj-cRjituc6xxbDDBhvVPP/view?usp=drive_link"
fran_triple_id ='1K0tGucwHLtEj-cRjituc6xxbDDBhvVPP'
fran_triple_id_url = 'https://drive.google.com/file/d/1K0tGucwHLtEj-cRjituc6xxbDDBhvVPP/preview'

fran_tenis_tiro = "https://drive.google.com/file/d/1BK67GKfpYiiNmUO30OHVlHCapsXdA1PG/view?usp=drive_link"
fran_tenis_id='1BK67GKfpYiiNmUO30OHVlHCapsXdA1PG'
fran_tenis_url='https://drive.google.com/file/d/1BK67GKfpYiiNmUO30OHVlHCapsXdA1PG/preview'
def app():
    st.markdown("# **CINEMATICA**")

    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Mostrar la primera tabla en la primera columna
    with col1:
        st.write("Tabla de datos del trackeo original de la pelota coordenadas fuera de eje")
        st.dataframe(data_chipi)

    # Mostrar la segunda tabla en la segunda columna
    with col2:
        st.write("Tabla de datos del trackeo con nuevo origen de coordenadas")
        st.dataframe(data_chipi_nuevo_origen)

    # ID del video en Google Drive
    video_id = '1yRrGMfC26jI2qizgLljeAp7saDFM4Atu'

    # Enlace embebido de Google Drive tiro del chipi
    video_url = 'https://drive.google.com/file/d/1yRrGMfC26jI2qizgLljeAp7saDFM4Atu/preview'

    # Enlace embebido del rebote contra el tablero
    video_rebote = 'https://drive.google.com/file/d/1QfBcWnunSSEiqFLoJtV2ViZKseZkzkwv/preview'

    video_id2 = '1QfBcWnunSSEiqFLoJtV2ViZKseZkzkwv'

    #Links a imagenes
    #   https://drive.google.com/file/d/1ukhRSp6qc5cBuhPTDhcBNPD3UEByNM0X/view?usp=drive_link
    #   https://drive.google.com/file/d/1J2mCgNWRncYrJFFkLD1fhXuPejJHQ4bD/view?usp=drive_link
    #   https://drive.google.com/file/d/1wv95827zG7UjuoZTrAqGBzF6GQQEYM2G/view?usp=drive_link

    # ID de la imagen en Google Drive
    grafico_tiro_doble="1ukhRSp6qc5cBuhPTDhcBNPD3UEByNM0X"
    grafico_tiro_tenis="1J2mCgNWRncYrJFFkLD1fhXuPejJHQ4bD"
    grafico_tiro_triple="1wv95827zG7UjuoZTrAqGBzF6GQQEYM2G"

    # Función para obtener la imagen desde Google Drive
    def get_image_from_drive(file_id):
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    # Título de la aplicación
    st.title("Video procesado del tiro hacia el aro de basquet")

    # Insertar el video usando HTML
    st.markdown(f"""
         <div style="text-align: center;">
              <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
          </div>
         """, unsafe_allow_html=True)

    # Agregar espacio después de la imagen
    st.title("Analisis del video de tiro")

    # Obtener y mostrar la imagen en Streamlit
    imagen_tiro_doble = get_image_from_drive(grafico_tiro_doble)
    st.image(imagen_tiro_doble, caption="Tiro doble Basquet")

    # Texto largo a mostrar con formato Markdown
    texto_tiro_doble = """
    **En nuestro sistema de referencias, el punto (0,0) se encuentra en el arranque de la curva del trackeo. Nuestros datos son los siguientes:**

    - **Tiempo de vuelo:** 0,93 segundos.
    - **Distancia en el eje X:** 3,71 m.
    - **Distancia en el eje Y:** 2,50 m.
    - **Altura del aro:** 3,05 m.
    - **Distancia desde el punto (0,0) al final del tiro:** 0,55 m.
    - **Distancia(0,0) Final Tiro = AlturaAro - DistanciaEjeY**.
    \n
    Ahora bien, para calcular la posición vertical y así encontrar 
    la velocidad inicial del tiro vertical, tenemos la siguiente ecuación:
    """
    # Mostrar el texto en Streamlit con Markdown
    st.markdown(texto_tiro_doble)
    # Ecuación en LaTeX
    latex_ec1 = r"""
    Y(t) = -\frac{1}{2} g t^2 + V_{0y} t + Y_0
    """
    st.latex(latex_ec1)
    st.write("\n\n")
    texto_sig="""
    Ahora bien, para calcular la altura máxima que alcanza el tiro, 
    debemos saber que esta se obtiene cuando la velocidad vertical es cero.
    Por lo tanto, utilizaremos la siguiente ecuación para calcular 
    el tiempo que tarda la pelota en alcanzar la altura máxima:
    """
    st.markdown(texto_sig)
    latex_ec2=r"""
    V_{y}=V_{0y}-gt
    """
    st.latex(latex_ec2)

    st.write("\n\n")
    texto_graf="""
        Observamos que los tres tiros corresponden al mismo experimento, con variaciones lógicas en sus resultados.
        Por lo tanto, ilustraremos los gráficos correspondientes al primer video.\n
        Establecimos que el origen del sistema de ejes cartesianos se ubicará en el primer frame 
        en el que se trackea la pelota. \n
        Luego, utilizamos el programa Curve Fit para ajustar los datos trackeados a un polinomio de segundo grado, 
        mejorando así la precisión de los datos.
        Recordemos que con Python trackeamos las coordenadas X y Y en píxeles en cada frame del video.
        En el siguiente gráfico se puede apreciar la diferencia entre los datos originales y
        los datos generados con el programa Curve Fit.
    """
    st.markdown(texto_graf)

    # Solicitar la imagen desde la URL
    response = requests.get(chipi_curvefit)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Curve Fit', use_column_width=True)


    col3, col4 = st.columns(2)
    # Mostrar la primera tabla en la primera columna
    with col3:
        st.write("Tabla de datos usando curvefit")
        st.dataframe(data_chipi_curvefit)

    texto_grafico_xy="""
    A continuación vemos el gráfico correspondiente la posición en los ejes X e Y de la pelota,
     diferenciando los cálculos teóricos de los datos trackeados en Python.
    """
    st.markdown(texto_grafico_xy)
    graf_posxy=requests.get(grafico_posxy)
    imgxy= Image.open(BytesIO(graf_posxy.content))
    st.image(imgxy, caption='Posicion X-Y', use_column_width=True)


    texto_velocidad=""" 
        A continuación vemos la evolución de la velocidad en el eje X a lo largo del tiempo.
        En teoría, la velocidad debería mantenerse constante, de acuerdo con la primera ley de Newton,
        que establece que la velocidad en X se mantiene constante si no hay fuerzas actuando
        en esa dirección. Sin embargo, en la práctica, observamos que la velocidad en X ha
        disminuido levemente debido a la fuerza de rozamiento con el aire, 
        que desacelera la pelota.
    """
    st.write("\n\n")
    st.markdown(texto_velocidad)
    graf_vel=requests.get(grafico_velocidad)
    imgv=Image.open(BytesIO(graf_vel.content))
    st.image(imgv, caption='Velocidad en X en el tiempo', use_column_width=True)

    st.write("\n\n")
    texto_aceleracion="""
       En el siguiente gráfico podemos ver que la aceleración en Y teórica debería ser igual a la gravedad. 
        Sin embargo, en los datos trackeados observamos una leve diferencia. 
        Al calcular un promedio de la aceleración en Y trackeada, obtenemos .
    """
    texto_velocidad_en_y="""
     En el siguiente gráfico podemos ver la velocidad en eje Y
    """
    st.markdown(texto_velocidad_en_y)
    graf_vel_y=requests.get(grafico_velocidad_y)
    imgvy=Image.open(BytesIO(graf_vel_y.content))
    st.image(imgvy, caption='Velocidad en Y en el tiempo', use_column_width=True)

    st.write("\n\n")
    st.markdown(texto_aceleracion)
    graf_acel=requests.get(grafico_aceleracion)
    imgac=Image.open(BytesIO(graf_acel.content))
    st.image(imgac,caption='Aceleracion en Y en el tiempo',use_column_width=True)

# BARRA SEPARDORA

    #st.title("Tiro con rebote al tablero")

    # Insertar el video usando HTML
    #st.markdown(f"""
    #      <div style="text-align: center;">
    #          <iframe src="{video_rebote}" width="640" height="480" allow="autoplay"></iframe>
    #      </div>
    #      """, unsafe_allow_html=True)

    # Solicitar la imagen desde la URL
    #response = requests.get(rebote_tablero_curvefit)
    #img = Image.open(BytesIO(response.content))
    #st.write("Grafico usando Curve Fit \n")
    #st.write("\n\n")

    # Mostrar la imagen en Streamlit
    #st.image(img, caption='Curve Fit', use_column_width=True)

    #col5, col6 = st.columns(2)
    #with col5:
    #    st.write("Tabla de datos usando curvefit")
    #    st.dataframe(data_rebote_tablero_curvefit)


    st.title("Tiro tenis de Fran")

    # Insertar el video usando HTML
    st.markdown(f"""
             <div style="text-align: center;">
                 <iframe src="{fran_tenis_url}" width="640" height="480" allow="autoplay"></iframe>
             </div>
             """, unsafe_allow_html=True)
    #
    st.write("\n\n")
    imagen_tiro_tenis = get_image_from_drive(grafico_tiro_tenis)
    st.image(imagen_tiro_tenis, caption="Tiro triple Tenis")

    st.title("Calculos y resultados")

    texto_triple="""
        En nuestro sistema de referencia, el punto (0,0) se encuentra en el inicio de la trayectoria del seguimiento.
        Nuestros datos son los siguientes:
        - **Tiempo de vuelo:** 1,266  segundos.
        - **Distancia en el eje X:** 6,19 m.
        - **Distancia en el eje Y:** 2,23 m.
        - **Altura del aro:** 3,05 m.
        - **Distancia desde el punto (0,0) al final del tiro:** 0,82  m.
    """
    st.markdown(texto_triple)

    imagen_tiro_triple=get_image_from_drive(grafico_tiro_triple)
    st.image(imagen_tiro_triple, caption="Tiro triple Triple")



