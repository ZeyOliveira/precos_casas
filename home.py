import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL


@st.cache_data
def carregar_dados_limpos():
    return pd.read_parquet(DADOS_LIMPOS)

@st.cache_data
def carregar_dados_geo():
    return gpd.read_parquet(DADOS_GEO_MEDIAN)

@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)


df = carregar_dados_limpos()
df_gpd = carregar_dados_geo()
modelo = carregar_modelo()


st.title("Previsão de preços de imóveis")

latitude = st.number_input("Latitude", value=-122.38)
longitude = st.number_input("Longitude", value=37.88)

housing_median_age = st.number_input("Idade do imóvel", value=10)
total_rooms = st.number_input("Total de cômodos", value=880)
total_bedrooms = st.number_input("Total de quartos", value=129)
population = st.number_input("População", value=322)
households = st.number_input("Domicílios", value=126)

median_income = st.slider(
    "Renda média (múltiplos de US$ 10k)", min_value=0.5, max_value=15.0, value=4.5, step=0.5
)

ocean_proximity = st.selectbox("Proximidade do Oceano", df["ocean_proximity"].unique())

median_income_cat = st.number_input("Categoria de Renda", value=4)

rooms_per_household = st.number_input("Quartos por Domicílio", value=6.99)
population_per_household = st.number_input("Pessoas por Domicílio", value=2.55)
bedrooms_per_room = st.number_input("Quartos por Cômodo", value=0.26)

entrada_modelo = {
    "latitude": latitude,
    "longitude": longitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    "ocean_proximity": ocean_proximity,
    "median_income_cat": median_income_cat,
    "rooms_per_household": rooms_per_household,
    "population_per_household": population_per_household,
    "bedrooms_per_room": bedrooms_per_room,
}

df_entrada_modelo = pd.DataFrame(entrada_modelo, index=[0])

botao_previsao = st.button("Prever preço")

if botao_previsao:
    preco = modelo.predict(df_entrada_modelo)
    st.write(f"Preço previsto: US$ {preco}")


