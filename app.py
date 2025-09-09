import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/juliandariogiraldoocampo/ia_taltech/main/fiscalia/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

seleccion_columnas = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

df_serie_tiempo = df.copy()
df_serie_tiempo['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

# CÁLCULO DE MUNICIPIO CON MAS DELITOS
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]



# CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="centered")
st.header("Dashboard de Delitos - Fiscalía")
st.dataframe(df)

st.markdown(f"<h3>Municipio con mas delitos: {max_municipio}</h3>", unsafe_allow_html=True)
st.markdown(f"<h3>Cantidad de Delitos: {max_cantidad_municipio}</h3>", unsafe_allow_html=True)

st.subheader("Tipo de Delito")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)