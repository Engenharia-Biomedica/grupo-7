#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:34:06 2023

@author: biancapeixoto
"""

base="dark"
primaryColor="#d4f1fb"
backgroundColor="#297e8e"
secondaryBackgroundColor="#3f828e"
font="monospace"


import streamlit as st
from PIL import Image

# carregando imagem para o logo
img = Image.open('Img.jpg')

# dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col = st.columns(3)

# colocando o logo na coluna central
with cent_col:
    st.header ('BACView') 
    
a_col, b_col, c_col, d_col, e_col = st.columns(5)
with a_col:                                    
    st.image(img, width=650)
   
# Texto introdutório
st.markdown("O BACView promove a visualização de dados a cerca da relação entre a resistência de bactérias e antibióticos - a um nível nacional. O menu a esquerda do site contém as categorias em exibição.")

