import streamlit as st
import streamlit.components.v1 as components
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

    st.markdown(
        """
        <a href="https://github.com/Chicago-Fisicos/proyecto-fisica/tree/main/src/basket-doble/tablas" class="custom-link">
           ✅ Este link tiene las tablas utilizadas en el proyecto
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.write("\n")

    st.markdown(
        """
        <a href="https://drive.google.com/file/d/1Lk_OBzktsQlqfI8Cjd8zH4MgffPiLC9E/view?usp=drive_link" class="custom-link">
            📑Nuestro informe.pdf
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.write("\n")

    st.markdown(
        """
        <a href="https://docs.google.com/presentation/d/1u7n7ahZckj_DDZmPV43kTO9ds10_vaWc/edit?usp=drive_link&ouid=111004064811447974858&rtpof=true&sd=true" class="custom-link">
           🎬 Y esta es nuestra presentacion 
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.write("\n\n")
    st.write("\n\n")

    components.iframe(
        "https://docs.google.com/presentation/d/e/2PACX-1vRI6PJMC0KnwygrjhoSusvv7sZmyfdZCHRS9JHUwln4XMK-5ePWmV8gY4dd24gM9Q/embed?start=false&loop=false&delayms=3000",
        height=600, width=800)

