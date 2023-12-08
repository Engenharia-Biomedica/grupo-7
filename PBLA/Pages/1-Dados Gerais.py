
import streamlit as st

import pandas as pd  # tratamento de dados
pd.options.mode.chained_assignment = None

import numpy as np  # ferramentas matemáticas

from datetime import datetime  # mensagem de greet no início

from IPython.display import display  # visualização dos dados


st.header ('Dados Gerais') 


# msg de greet
now = datetime.now()
print(f'\n\n>> {now} : Código Rodando!\n')

# função de checagem procedural
def check(x,y):    
    print('\n\n>> display df\n')
    display(x)
    print('\n\n')
    if y == 1:
        exit()


print('\n>> Lendo DF até a linha 500...\n')
# abrindo o arquivo
file = "dados_certo.xlsx"
data = pd.read_excel(file, nrows = 500)  


print('\n>> Truncando e renomeando colunas de DF ...\n')
# novo df com 3 colunas: tempo x bac x resist
df = data[['dh_prescricao_lancamento','ds_micro_organismo','cd_interpretacao_antibiograma']].copy(deep=True)   # deep copy p não alterar os dados originais
df.rename(columns={"dh_prescricao_lancamento": "tempo", "ds_micro_organismo": "microorganismo", "cd_interpretacao_antibiograma": "status"}, inplace=True)
check(df,0)  # checando o df, sem quitar o código


print('\n>> limpando e organizando os dados:\n')
print('\n\t>> removendo entradas nulas...')
df.dropna(subset=['status'],inplace=True)
check(df,0)  # checando o df, sem quitar o código


# truncando os valores de data para somente ANO-MES-DIA
print('\n\t>> truncando as datas...')
df['tempo'] = pd.to_datetime(df['tempo'])
check(df,0)  # checando o df, sem quitar o código


print('\n\t>> fazendo substituições na coluna de resistência...')
df.replace(to_replace={"Sensível" : 0, "Sensível Aumentando Exposição" : 1, "Sensível Dose-Dependente" : 1, "Resistente" : 2},inplace=True)
check(df,0)  # checando o df, sem quitar o código


print('\n>> definindo a função de cálculo de score...\n')
def score(status_values):
    return np.mean(status_values)


print('\n>> Criando novo df, agrupado por dia e por microorganismo, através da função score...\n')
result_df = df.groupby([df['tempo'].dt.date, 'microorganismo']).agg({'status': score}).reset_index()


print('\n>> DF Final:')
check(result_df,0)  # checando o df, sem quitar o código
