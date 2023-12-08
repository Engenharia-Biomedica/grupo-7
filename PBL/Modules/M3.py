#  ----------------------------------------------
#  Módulo 3:  Base do tratamento de dados
#  ----------------------------------------------# Importa as bibliotecas necessÃ¡rias
import streamlit as st
import pandas as pd
import pydeck as pdk

# Inicializa uma lista vazia chamada BaseDados
BaseDados = []

# Lê o DataFrame a partir do arquivo Excel chamado 'endeinstein.xlsx'
df = pd.read_excel('endeinstein.xlsx')

# Loop sobre cada linha do DataFrame
for i in range(len(df)):

    # Obtem as colunas 'Latitude' e 'Longitude' para cada linha
    Latitude = (df.at[i,'Latitude'])
    Longitude = (df.at[i,'Longitude'])
    Infectados = (df.at[i,'Quantidade'])
    
    # Cria uma lista chamada Coordenadas com a latitude e longitude
    Coordenadas = [Latitude,Longitude]
    
    # Inicializa uma variável n com o valor 1
    n = 1
        
    # Loop para adicionar as coordenadas à lista BaseDados de acordo com o nÃºmero de infectados
    while n <= Infectados:
        BaseDados.append(Coordenadas)
        n = n + 1

# Cria um DataFrame chamado chart_data a partir da lista BaseDados
chart_data = pd.DataFrame((BaseDados), columns=['Latitude','Longitude'])

# Usa Streamlit para exibir um gráfico PyDeck na interface
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-23.61,
        longitude=-46.71,
        zoom=11,
        pitch=50,
    ),
    layers=[
        # Adiciona uma camada HexagonLayer ao mapa
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[Longitude, Latitude]',
            auto_highlight=True,
            radius=200,
            elevation_scale=5,
            elevation_range=[0, 500],
            pickable=True,
            extruded=True,
        ),
        # Adiciona uma camada ScatterplotLayer ao mapa
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[Longitude, Latitude]',
            get_color='[30, 0, 160]',  # Cor em RGB
            get_radius=100,
        ),
    ],
))
