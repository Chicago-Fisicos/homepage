import streamlit as st

def app():
    st.markdown("# **ANEXO**")

    # Enlace embebido del documento de Google Docs
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vQoa5ydrBaC1pbo_RJ8cRkg0fy9j7LmTTw0JwG_wvDQFZXClui8aE7W0SUixhkGzeUaqxM6pC2D7bDc/pub"

    # Mostrar el documento de Google Docs en Streamlit usando un iframe
    st.markdown(f'<iframe src="{doc_url}" width="700" height="1000"></iframe>', unsafe_allow_html=True)