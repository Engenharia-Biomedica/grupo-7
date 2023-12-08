#  ----------------------------------------------
#  Módulo 4:  Base do tratamento de dados
#  ----------------------------------------------
# Importa a biblioteca pandas com o alias pd
import pandas as pd

# Define o caminho do arquivo Excel
filepath = 'dados_importantes.xlsx'

# Lê os dados do arquivo Excel e os armazena na variável 'dados'
dados = pd.read_excel(filepath) 

# Filtra os dados para incluir apenas linhas com unidades de coleta específicas
locais_filtrados = dados[(dados['ds_unidade_coleta'] == 'HIAE Morumbi')\
                         | (dados['ds_unidade_coleta'] == 'Santa Catarina') \
                         | (dados['ds_unidade_coleta'] == 'Alphaville') \
                         | (dados['ds_unidade_coleta'] == 'Perdizes') \
                         | (dados['ds_unidade_coleta'] == 'Ibirapuera') \
                         | (dados['ds_unidade_coleta'] == 'Jardins') \
                         | (dados['ds_unidade_coleta'] == 'Alto de Pinheiros') \
                         | (dados['ds_unidade_coleta'] == 'Chacara Klabin') \
                         | (dados['ds_unidade_coleta'] == 'Vila Mariana') \
                         | (dados['ds_unidade_coleta'] == 'HIAE') \
                         | (dados['ds_unidade_coleta'] == 'B sangue HIAE')]

# Seleciona colunas específicas dos dados filtrados
informacoes_filtrados = locais_filtrados[['ds_unidade_coleta',\
                                          'dh_coleta_exame',\
                                          'ds_micro_organismo',\
                                          'ds_antibiotico_microorganismo',\
                                          'cd_interpretacao_antibiograma',\
                                          'id_prontuario']]

# Imprime os dados filtrados na tela
print('\ninformacoes_filtrados\n')
print(informacoes_filtrados, '\n')

# Agrupa os dados e conta a quantidade única de 'id_prontuario' para cada grupo
id_uni_micro = informacoes_filtrados.groupby(['ds_micro_organismo','ds_unidade_coleta']).nunique()['id_prontuario']

# Imprime os dados agrupados na tela
print('\nDados Agrupados - Contagem de Resultados por Antibiótico\n')
print(id_uni_micro, '\n')

# Reseta o índice e imprime novamente os dados agrupados
transform_colunas = id_uni_micro.reset_index(drop=False)
print('\nDados Agrupados - Perfil Anual de Resistencia aos Antibióticos - voltando index para columns\n')
print(transform_colunas, '\n')

# Realiza uma nova filtragem para incluir apenas linhas onde 'ds_micro_organismo' é igual a 'Candida albicans'
bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Candida albicans')]
print(bot_t)
