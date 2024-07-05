import streamlit as st

def app():

    # Enlace del PDF en Google Drive
    pdf_url = "https://drive.google.com/file/d/1FVxZyBev1lXaggrdcJmPjjjjxyI380sT/preview"

    st.title('Informe final')

    # Ajustar el tamaño del iframe y agregar estilo CSS para mejor visualización
    st.markdown(
        f"""
        <style>
        .iframe-container {{
            position: relative;
            overflow: hidden;
            width: 100%;
            padding-top: 75%; /* Ajustar la relación de aspecto aquí */
        }}
        .iframe-container iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        </style>
        <div class="iframe-container">
            <iframe src="{pdf_url}" allowfullscreen></iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )

app()
