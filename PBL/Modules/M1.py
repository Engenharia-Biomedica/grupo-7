#  -----------------------------------------------------------------
#  Módulo 1:  Upload de arquivos
#  -----------------------------------------------------------------

import pandas as pd  # tratamento de dados
import numpy as np  # ferramentas matemáticas
import openpyxl
import streamlit as st

def importFile (file):
    data = ''
    # abrindo o arquivo
    countError = 0
    try:
        wb_openpyxl = openpyxl.load_workbook(file)
        ws_openpyxl = wb_openpyxl.active
        columns = [cell.value for cell in ws_openpyxl[1]]
        data_openpyxl = ws_openpyxl.iter_rows(min_row=2, values_only=True)
        data = pd.DataFrame(data_openpyxl, columns=columns)
    except:
        print(f"Não foi possível ler o arquivo.")
        print(f"error = {countError}.")
        countError = 1

    if countError == 0:
        print(f'countError = {countError}')
        return data

    else:
        print("Encerrando...")
        print(f'countError = {countError}')
        return countError    
    
def upload(x):
    file = importFile (x)
    return file

