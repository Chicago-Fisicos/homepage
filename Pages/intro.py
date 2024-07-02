import streamlit as st

# ---->
# Links utilizados:
#                   https://drive.google.com/uc?export=download&id=1RWtqI_ZqExIyvrCIzwQQmMt0qDv67mHY

def app():
    st.markdown("<h1 style='text-align: center; color: white;'>CHICAGO FISICOS</h1>", unsafe_allow_html=True)

    st.markdown("### **Ayudante: Marcos Meo**")

    texto="""
        - María Luz Cabral
        - Nahuel Diaz
        - Franco Tomás Cippitelli
        - Francisco Luis Flaibani
        - Brenda Belen Martinez Ocampo
        - Yohana Moyano
        - Matías David Schwerdt
        - Jeremias Eloy Segurado Negrin
        - Santiago Vazquez
        - Diego José Villarroel
    """
    st.markdown(texto)

    texto_intro="""
        El básquet es uno de los deportes más populares y practicados en el mundo, con un alcance global que atrae a millones de seguidores.
        Este deporte se caracteriza por estar profundamente arraigado en los principios físicos, los cuales inciden de manera significativa
        en cada acción dentro de la cancha.\n
        En el presente informe, nos adentraremos en el análisis de la interacción entre la física y el básquet, examinando su impacto en los aspectos fundamentales del juego.
        Como el Grupo “Chicago Físicos”, conformado por diez estudiantes de Ingeniería en Sistemas, 
        nos hemos propuesto el desafío de analizar y demostrar la relevancia de la física en el básquet.\n
         A lo largo de este estudio, abordaremos una amplia gama de temas de Física I, llevándolos de la teoría a la práctica a través
        de experimentos y pruebas realizadas directamente en el contexto del básquet.\n
        Nos basaremos en contenido multimedia generado por nosotros mismos para documentar nuestras investigaciones, utilizando el lenguaje
        de programación Python para realizar cálculos precisos y desarrollar herramientas que nos permitan profundizar en nuestro análisis.
        A lo largo de este informe, explicaremos temas clave como la cinemática, la dinámica, energía y choque. Con este enfoque multidisciplinario,
        esperamos arrojar luz sobre la intrincada interacción entre la ciencia y el deporte, demostrando cómo el conocimiento de la física puede
        enriquecer nuestra comprensión y apreciación del básquet en todas sus facetas.
    """
    st.markdown("## **Introduccion**")
    st.markdown(texto_intro)