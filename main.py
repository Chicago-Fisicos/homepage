import streamlit as st
import pandas as pd

st.write("Chicago Fisicos")

url = ("https://raw.githubusercontent.com/95sv/repo_fisica/main/chewer.csv")

df = pd.read_csv(url, delimiter=',')

st.dataframe(df)