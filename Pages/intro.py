import streamlit as st

# ---->
# Links utilizados:
#                   https://drive.google.com/uc?export=download&id=1RWtqI_ZqExIyvrCIzwQQmMt0qDv67mHY

def app():

    # HTML para centrar el título con más estilos
    html_title = """
    <div style="text-align: center; font-size: 32px; color: #FBF7FA; font-weight: bold; margin-top: 20px;">
        CHICAGO FISICOS
    </div>
    """

    # Renderizar el HTML en Streamlit
    st.markdown(html_title, unsafe_allow_html=True)

    # Continuar con el resto de tu aplicación
    st.title("Proyecto de Fisica I")

    st.write("Ayudante: Marcos Meo")

    st.write("María Luz Cabral" )
    st.write("Nahuel Diaz")
    st.write("Franco Tomás Cippitelli")
    st.write("Francisco Luis Flaibani")
    st.write("Brenda Belen Martinez Ocampo")
    st.write("Yohana Moyano")
    st.write("Matías David Schwerdt")
    st.write("Jeremias Eloy Segurado Negrin")
    st.write("Santiago Vazquez")
    st.write("Diego José Villarroel")