import pydeck as pdk
import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import shapely

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL


@st.cache_data
def carregar_dados_limpos():
    return pd.read_parquet(DADOS_LIMPOS)

@st.cache_data
def carregar_dados_geo():
    df_gpd = gpd.read_parquet(DADOS_GEO_MEDIAN)   # Carrega o arquivo 'parquet' contendo os dados geoespaciais.

    df_gpd = df_gpd.explode(ignore_index=True) # Se houver geometrias MultiPolygon, esta função transforma cada parte em uma linha separada no dataframe.

    
    def fixar_e_orientar_geometry(geometry):
        if not geometry.is_valid:
            geometry = geometry.buffer(0) #  Corrige possíveis problemas na geometria.

        if isinstance(
            geometry, (shapely.geometry.Polygon, shapely.geometry.MultiPolygon)
        ):
            geometry = shapely.geometry.polygon.orient(geometry, sign=1.0)  # Ajusta a orientação.
        return geometry


    df_gpd["geometry"] = df_gpd["geometry"].apply(fixar_e_orientar_geometry)


    def obter_coordenadas_polyg(geometry):
        return(
            [[[x, y] for x, y in geometry.exterior.coords]]  # Se a geometria for um Polígono, extrai as coordenadas externas.
            
            if isinstance(geometry, shapely.geometry.Polygon) # Se for um MultiPolygon, percorre cada polígono e extrai as coordenadas externas de cada um.

            else[
                [[x, y] for x, y in polygon.exterior.coords]
                for polygon in geometry.geoms
            ]
        )


    df_gpd['geometry'] = df_gpd['geometry'].apply(obter_coordenadas_polyg)

    return df_gpd


@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)



df = carregar_dados_limpos()
df_gpd = carregar_dados_geo()
modelo = carregar_modelo()




st.title("Previsão de preços de imóveis")

condados = sorted(df_gpd["name"].unique())   # Lista ordenada dos nomes dos condados.

coluna1, coluna2 = st.columns(2)

with coluna1:
    with st.form(key='formulario'):
        condado_selecionado = st.selectbox("Condado", options=condados)   # Condados selecionado pelo usuário na "home".
        
        latitude = df_gpd.query("name == @condado_selecionado")['latitude'].values # Filtrando o GeoPandasDF pelo nome do condado selecionado, e retornando específicamente o valor da coluna "latitude".
        
        
        longitude = df_gpd.query("name == @condado_selecionado")['longitude'].values # A mesma coisa!, porém retornando o valor da coluna "longitude".
        
        housing_median_age = st.number_input(
            "Idade do imóvel", 
            value=10,
            min_value=df["housing_median_age"].min(),
            max_value=df["housing_median_age"].max()
        )
        
        
        total_rooms = df_gpd.query("name == @condado_selecionado")['total_rooms'].values
        total_bedrooms = df_gpd.query("name == @condado_selecionado")['total_bedrooms'].values
        population = df_gpd.query("name == @condado_selecionado")['population'].values
        households = df_gpd.query("name == @condado_selecionado")['households'].values
        
        
        median_income = st.slider(
            "Renda média (milhares de US$)",
            min_value=5.0,
            max_value=104.0,
            value=45.0,
            step=5.0
        )
        
        ocean_proximity = df_gpd.query("name == @condado_selecionado")['ocean_proximity'].values
        
        bins_income = [0, 1.5, 3, 4.5, 6, np.inf]
        median_income_cat = np.digitize(median_income / 10, bins=bins_income)
        
        rooms_per_household = df_gpd.query("name == @condado_selecionado")['rooms_per_household'].values
        population_per_household = df_gpd.query("name == @condado_selecionado")['population_per_household'].values
        bedrooms_per_room = df_gpd.query("name == @condado_selecionado")['bedrooms_per_room'].values
        
        entrada_modelo = {
            "latitude": latitude,
            "longitude": longitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income / 10,
            "ocean_proximity": ocean_proximity,
            "median_income_cat": median_income_cat,
            "rooms_per_household": rooms_per_household,
            "population_per_household": population_per_household,
            "bedrooms_per_room": bedrooms_per_room,
        }
        
        df_entrada_modelo = pd.DataFrame(entrada_modelo)
        
        botao_previsao = st.form_submit_button("Prever preço")
    
    if botao_previsao:
        preco = modelo.predict(df_entrada_modelo)
        st.metric(label="Preço previsto: (US$)", value=f"{preco[0][0]:,.2f}")


with coluna2:
    view_state = pdk.ViewState(
        latitude=float(latitude[0]),
        longitude=float(longitude[0]),
        zoom=5,
        min_zoom=5,
        max_zoom=15,
    )

    polygon_layer = pdk.Layer(
        "PolygonLayer",
        data=df_gpd[['name', 'geometry']],
        get_polygon='geometry',
        get_fill_color=[0, 0, 255, 100],
        get_line_color=[255, 255, 255],
        get_line_width=50,
        pickable=True,
        auto_highlight=True,
    )

    selecionado_condado = df_gpd.query("name == @condado_selecionado")
    
    highlight_layer = pdk.Layer(
        "PolygonLayer",
        data= selecionado_condado[['name', 'geometry']],
        get_polygon='geometry',
        get_fill_color=[255, 0, 0, 100],
        get_line_color=[0, 0, 0],
        get_line_width=500,
        pickable=True,
        auto_highlight=True,
    )

    tooltip = {
        "html": "<b>Condado:</b> {name}",
        "style":{"backgroundColor": "steelblue", "color": "white", "fontsize": "10px"}
    }

    mapa = pdk.Deck(
        initial_view_state=view_state,
        map_style='light',
        layers=[polygon_layer, highlight_layer],
        tooltip=tooltip,
    )

    st.pydeck_chart(mapa)
