#  -----------------------------------------
#  Módulo 5:  Exportação com "Botão" 
#  -----------------------------------------
# Importa a biblioteca pandas
import pandas as pd


# Define uma função para exportar dados a partir de um arquivo Excel
def exportar_dados(filepath):
    
    # Leitura do arquivo Excel e armazenamento dos dados no DataFrame 'dados'
    dados = pd.read_excel(filepath)

    # Filtra as linhas do DataFrame com base na coluna 'ds_unidade_coleta'
    locais_filtrados = dados[(dados['ds_unidade_coleta'] == 'HIAE Morumbi') \
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

    # Seleciona colunas específicas para criar um novo DataFrame
    informacoes_filtrados = locais_filtrados[['ds_unidade_coleta', \
                                              'dh_coleta_exame', \
                                              'ds_micro_organismo', \
                                              'ds_antibiotico_microorganismo', \
                                              'cd_interpretacao_antibiograma', \
                                              'id_prontuario']]

    # Realiza o agrupamento dos dados e conta a quantidade única de 'id_prontuario'
    id_uni_micro = informacoes_filtrados.groupby(['ds_micro_organismo', 'ds_unidade_coleta']).nunique()['id_prontuario']

    # Reseta o índice do DataFrame resultante do agrupamento
    transform_colunas = id_uni_micro.reset_index(drop=False)

    # Exemplo de filtro adicional
    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Streptococcus pneumoniae')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Candida albicans')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Achromobacter xylosoxidans')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Aeromonas hydrophila')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Canalb')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Aeromonas caviae')]
#    bot_t = transform_colunas[(transform_colunas['ds_micro_organismo'] == 'Acinetobacter gyllenbergii')]

    # Retorna os DataFrames resultantes para possível análise ou uso externo
    return informacoes_filtrados, id_uni_micro, transform_colunas, bot_t

# Caminho do arquivo Excel
filepath = 'dados_importantes.xlsx'

# Chama a função exportar_dados e obtém os resultados
exportar_dados(filepath)
