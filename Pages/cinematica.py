import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

chipi_trackeo_original = ("https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-original.csv")
chipi_trackeo_nuevo_origen = ("https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-original-nuevo-origen.csv")
chipi_curvefit = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/curve_fit.png?raw=true'
chipi_savitzky = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/basket-doble/graficos/savitzky.png?raw=true'
chipi_tabla_curvefit= 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-suavizado-curve-fit-nuevo-origen.csv'
chipi_tabla_savitzky ='https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/basket-doble/tablas/trackeo-suavizado-savitzky-nuevo-origen.csv'

rebote_tablero_curvefit = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/descartado/basket-rebote-tablero/graficos/curve_fit.png?raw=true'
rebote_tablero_savitzky ='https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/descartado/basket-rebote-tablero/graficos/savitzky.png?raw=true'
rebote_tabla_nuevo_origen = 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/descartado/basket-rebote-tablero/tablas/trackeo-original-nuevo-origen.csv'
rebote_tabla_curvefit = 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/descartado/basket-rebote-tablero/tablas/trackeo-suavizado-curve-fit-nuevo-origen.csv'
rebote_tabla_savitzky = 'https://raw.githubusercontent.com/Chicago-Fisicos/proyecto-fisica/main/src/descartado/basket-rebote-tablero/tablas/trackeo-suavizado-savitzky-nuevo-origen.csv'

data_chipi = pd.read_csv(chipi_trackeo_original, delimiter=',')
data_chipi_nuevo_origen = pd.read_csv(chipi_trackeo_nuevo_origen,delimiter =',')
data_chipi_curvefit = pd.read_csv(chipi_tabla_curvefit,delimiter =',')
data_chipi_savitzky = pd.read_csv(chipi_tabla_curvefit,delimiter =',')

data_rebote_tablero_curvefit = pd.read_csv(rebote_tabla_curvefit, delimiter =',')
data_rebote_tablero_savitzky = pd.read_csv(rebote_tabla_savitzky, delimiter =',')

def app():
    st.write("CINEMATICA")

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
    st.write("Grafico usando curvefit \n")
    st.write("\n\n")

    # Solicitar la imagen desde la URL
    response = requests.get(chipi_curvefit)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Curve Fit', use_column_width=True)

    st.write("Grafico usando savitzky \n")
    st.write("\n\n")

    # Solicitar la imagen desde la URL
    response = requests.get(chipi_savitzky)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Savityzky', use_column_width=True)

    col3, col4 = st.columns(2)
    # Mostrar la primera tabla en la primera columna
    with col3:
        st.write("Tabla de datos usando curvefit")
        st.dataframe(data_chipi_curvefit)

    # Mostrar la segunda tabla en la segunda columna
    with col4:
        st.write("Tabla de datos usando Savitzky")
        st.dataframe(data_chipi_savitzky)

    st.title("Tiro con rebote al tablero")

    # Insertar el video usando HTML
    st.markdown(f"""
          <div style="text-align: center;">
              <iframe src="{video_rebote}" width="640" height="480" allow="autoplay"></iframe>
          </div>
          """, unsafe_allow_html=True)

    # Solicitar la imagen desde la URL
    response = requests.get(rebote_tablero_curvefit)
    img = Image.open(BytesIO(response.content))
    st.write("Grafico usando Curve Fit \n")
    st.write("\n\n")

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Curve Fit', use_column_width=True)

    response = requests.get(rebote_tablero_savitzky)
    img = Image.open(BytesIO(response.content))
    st.write("Grafico usando Savitzky \n")
    st.write("\n\n")
    # Mostrar la imagen en Streamlit
    st.image(img, caption='Savitzky', use_column_width=True)

    col5, col6 = st.columns(2)
    with col5:
        st.write("Tabla de datos usando curvefit")
        st.dataframe(data_rebote_tablero_curvefit)

    # Mostrar la segunda tabla en la segunda columna
    with col6:
        st.write("Tabla de datos usando Savitzky")
        st.dataframe(data_rebote_tablero_savitzky)