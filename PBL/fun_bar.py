

def grafico_barra(): 
    
    import pandas as pd

    # Carregando os dados do Excel
    caminho_excel = 'dados_importantes(3).xlsx'
    dados = pd.read_excel(caminho_excel)

    # Contando a frequência de cada combinação de antibiótico e bactéria
    contagem_combinacoes = dados.groupby(['ds_antibiotico_microorganismo', 'ds_micro_organismo']).size().reset_index(name='Contagem')

    # Calculando a porcentagem para cada combinação
    contagem_combinacoes['Porcentagem'] = (contagem_combinacoes['Contagem'] / contagem_combinacoes.groupby('ds_antibiotico_microorganismo')['Contagem'].transform('sum')) * 100

   