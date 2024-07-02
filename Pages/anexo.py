import streamlit as st

def app():
    st.markdown("# **ANEXO**")

    # Enlace embebido del documento de Google Docs
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vQoa5ydrBaC1pbo_RJ8cRkg0fy9j7LmTTw0JwG_wvDQFZXClui8aE7W0SUixhkGzeUaqxM6pC2D7bDc/pub"

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
            <iframe src="{doc_url}" allowfullscreen></iframe>
        </div>
        """,
        unsafe_allow_html=True,
    )