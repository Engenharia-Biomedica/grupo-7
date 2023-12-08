#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:46:59 2023

@author: biancapeixoto
"""

import pandas as pd
import streamlit as st

st.header ('Dados por Locais') 


# Carregando os dados do Excel
caminho_excel = 'dados_importantes(3).xlsx'
dados = pd.read_excel(caminho_excel)

# Contando a frequência de cada combinação de antibiótico e bactéria
contagem_combinacoes = dados.groupby(['ds_antibiotico_microorganismo', 'ds_micro_organismo']).size().reset_index(name='Contagem')

# Calculando a porcentagem para cada combinação
contagem_combinacoes['Porcentagem'] = (contagem_combinacoes['Contagem'] / contagem_combinacoes.groupby('ds_antibiotico_microorganismo')['Contagem'].transform('sum')) * 100

# Criando um gráfico de barras diretamente com o pandas
grafico = contagem_combinacoes.pivot(index='ds_antibiotico_microorganismo', columns='ds_micro_organismo', values='Porcentagem').plot(kind='bar', stacked=True, figsize=(12, 6))

# Adicionando rótulos e título
grafico.set_xlabel('Bactéria')
grafico.set_ylabel('Porcentagem (%)')
grafico.set_title('Porcentagem de Antibióticos por Bactéria')
grafico.legend(title='Antibiótico', bbox_to_anchor=(1.05, 1), loc='upper left')

# Rotacionando os rótulos no eixo x para melhor legibilidade, se necessário
grafico.set_xticklabels(grafico.get_xticklabels(), rotation=45, ha='right')

# Exibindo o gráfico usando Streamlit
st.pyplot(grafico.get_figure())