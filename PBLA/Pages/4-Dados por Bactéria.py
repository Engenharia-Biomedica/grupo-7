import pandas as pd
import streamlit as st

st.header ('Dados por Bactéria') 

# Carregando os dados do Excel
caminho_excel = 'dados_certo.xlsx'
dados = pd.read_excel(caminho_excel)

# Adicionando uma opção de seleção para escolher uma bactéria
bacteria_selecionada = st.selectbox('Escolha uma bactéria:', dados['ds_micro_organismo'].unique())

# Filtrando os dados com base na bactéria selecionada
dados_filtrados = dados[dados['ds_micro_organismo'] == bacteria_selecionada]

# Contando a frequência de cada combinação de antibiótico e bactéria nos dados filtrados
contagem_combinacoes = dados_filtrados.groupby(['ds_antibiotico_microorganismo', 'ds_micro_organismo']).size().reset_index(name='Contagem')

# Calculando a porcentagem para cada combinação nos dados filtrados
contagem_combinacoes['Porcentagem'] = (contagem_combinacoes['Contagem'] / contagem_combinacoes.groupby('ds_micro_organismo')['Contagem'].transform('sum')) * 100

# Criando um gráfico de barras diretamente com o pandas
grafico = contagem_combinacoes.pivot(index='ds_antibiotico_microorganismo', columns='ds_micro_organismo', values='Porcentagem').plot(kind='bar', stacked=True, figsize=(12, 6))

# Adicionando rótulos e título
grafico.set_xlabel('Antibiótico')
grafico.set_ylabel('Porcentagem (%)')
grafico.set_title(f'Porcentagem de Antibióticos para a Bactéria: {bacteria_selecionada}')
grafico.legend(title='Bactéria', bbox_to_anchor=(1.05, 1), loc='upper left')

# Rotacionando os rótulos no eixo x para melhor legibilidade, se necessário
grafico.set_xticklabels(grafico.get_xticklabels(), rotation=45, ha='right')

# Exibindo o gráfico usando Streamlit
st.pyplot(grafico.get_figure())