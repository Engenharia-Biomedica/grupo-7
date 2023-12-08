#  -----------------------------------------
#  Módulo 7:  Plot Aeromonas Cavie
#  -----------------------------------------
# Importa as bibliotecas necessÃ¡rias
import streamlit as st
import pandas as pd
import pydeck as pdk
from func_dados import exportar_dados

filepath = 'dados_importantes.xlsx'
informacoes_filtrados, id_uni_micro, transform_colunas, bot_t = exportar_dados(filepath)


# Inicializa uma lista vazia chamada BaseDados
BaseDados = []

#print(bot_t)

#  o DataFrame a partir do arquivo Excel chamado 'Endereços_Einstein.xlsx'
df = pd.read_excel('Endereços_Einstein.xlsx')

nUnid = 0
totinfec=0
# Loop sobre cada linha do DataFrame
for i in range(len(df)):

    unid = (df.at[i, 'Unidade'])

    # Obtem as colunas 'Latitude' e 'Longitude' para cada linha
    Latitude = (df.at[i,'Latitude'])
    Longitude = (df.at[i,'Longitude'])
    infectados=0
    
    # 'Aeromonas Caviae'
    for i in range(4,9,1):
        unid1=bot_t.at[i, 'ds_unidade_coleta']
        if unid1 == unid:
           infectados = bot_t.at[i, 'id_prontuario']   
           totinfec = totinfec + infectados

    # Cria uma lista chamada Coordenadas com a latitude e longitude
    Coordenadas = [Latitude,Longitude]
    

    if unid != "Referencia" and  unid != "Referência1":
       nUnid= nUnid + 1
    elif unid == "Referencia":
        infectados=1
    elif unid == "Referencia1":         
        infectados=int(totinfec/9)
        
    #print(unid,infectados,totinfec,Coordenadas)    
        
    # Inicializa uma variável n com o valor 1
    n = 1
    # Loop para adicionar as coordenadas ÃÂ  lista BaseDados de acordo com o nÃºmero de infectados
    while n <= infectados:
        BaseDados.append(Coordenadas)
        n = n + 1

# Cria um DataFrame chamado chart_data a partir da lista BaseDados
chart_data = pd.DataFrame((BaseDados), columns=['Latitude','Longitude'])

#print(chart_data)

# Usa Streamlit para exibir um grÃÂ¡fico PyDeck na interface
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
