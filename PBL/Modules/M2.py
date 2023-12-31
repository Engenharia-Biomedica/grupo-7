#  -----------------------------------------------------------------
#  Módulo 2:  Conversão de endereço em coordenada geográfica
#  -----------------------------------------------------------------
### Importação de bibliotecas ###

#Importando biblioteca para criar aplicativos da web interativos com Python.
import streamlit as st

#Importando biblioteca de análise de dados.
import pandas as pd

#Importando extensão do pandas para lidar com dados geoespaciais.
import geopandas as gpds

### Inicialização de listas e leitura de dados ###

#Inicialização de listas vazias para armazenar coordenadas.
coordenadas = []

#Inicialização de listas vazias para armazenar latitude.
latitude=[]

#Inicialização de listas vazias para armazenar longitude.
longitude=[]

### Acessando o Banco de dados para análise

#Leitura de um arquivo Excel chamado 'Endereços_Einstein.xlsx' usando o pandas e armazenamento dos dados em um DataFrame chamado df.
df = pd.read_excel('Endereços_Einstein.xlsx')

### Geocodificação de endereços ###

# Utilização do Geopandas para geocodificar os endereços do DataFrame 'df', utilizando o serviço 'Nominatim'. 
# As coordenadas resultantes são armazenadas na lista 'coordenadas'.
coordenadas = gpds.tools.geocode(df['Endereço'], provider="nominatim", user_agent="home")["geometry"]

### Extração de latitude e longitude ###

# Iteração sobre as coordenadas geocodificadas, convertendo cada coordenada para string e extraindo a latitude e 
# a longitude a partir dos índices específicos na string. Esses valores são convertidos para float e armazenados nas listas latitude e longitude.
for coordenada in coordenadas:

    coordenada = str(coordenada)

    latitude.append(float(coordenada[19:29]))
    longitude.append(float(coordenada[7:17]))

### Definindo os pontos para criação do mapa ###

# Criação de um DataFrame chamado data com valores de latitude e longitude extraídos dos primeiros quatro registros.
data = pd.DataFrame({
    'latitude': [latitude[0], latitude[1], latitude[2], latitude[3]],
    
    'longitude': [longitude[0], longitude[1], longitude[2], longitude[3]]
})

### Gerando um mapa com os pontos extraídos do meu banco de dados ###
#Utilização do Streamlit para criar e exibir um mapa interativo com base nos dados de latitude e longitude no DataFrame data.
st.map(data)
