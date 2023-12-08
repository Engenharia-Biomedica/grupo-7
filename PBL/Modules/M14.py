#  ------------------------------------------------------------------
#  Módulo 14:  Plot Resistência Adquirida x Bactéria x Tempo
#  ------------------------------------------------------------------
import pandas as pd  # tratamento de dados
import numpy as np  # ferramentas matemáticas
import openpyxl
import uServ0 as S0

def grafLinha(file):
    x = S0.importFile(file)
    if type(x) == int:
        return x
    else:
        data = x
        
        
    # novo df com 3 colunas: tempo x bac x resist
    df = data[['dh_prescricao_lancamento','ds_micro_organismo','cd_interpretacao_antibiograma']].copy(deep=True)   # deep copy p não alterar os dados originais
    df.rename(columns={"dh_prescricao_lancamento": "tempo", "ds_micro_organismo": "microorganismo", "cd_interpretacao_antibiograma": "status"}, inplace=True)

    df = df.dropna(subset=['status']).reset_index()
    df = df[~df['status'].isin(['Não aplicável', 'Negativo'])]

    # truncando os valores de data para somente ANO-MES-DIA
    df['tempo'] = pd.to_datetime(df['tempo'])

    df.replace(to_replace={"Sensível" : 0, "Sensível Aumentando Exposição" : 1, "Sensível Dose-Dependente" : 1, "Resistente" : 2},inplace=True)

    def score(status_values):
        return np.mean(status_values)

    result_df = df.groupby([df['tempo'].dt.day, 'microorganismo']).agg({'status': score}).reset_index()

    return result_df
