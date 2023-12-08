#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:23:46 2023

@author: biancapeixoto
"""

import pandas as pd
import streamlit as st
from PIL import Image

# carregando imagem para o logo
img1 = Image.open('An.jpeg')
img2 = Image.open('Bi.jpeg')
img3 = Image.open('Duff.jpeg')
img4 = Image.open('Ju.jpeg')
img5 = Image.open('Ra.jpeg')
img6 = Image.open('Ot.jpeg')
                  
st.header ('Made by') 
    
a_col, b_col, c_col, d_col, e_col = st.columns(5)
with b_col:                                    
    st.image(img1, width=200)
    st.markdown('Antonio Faiçal')
    
    st.image(img2, width=200)
    st.markdown('Bianca Peixoto')
    
    st.image(img3, width=200)
    st.markdown('Eduardo de Angelis')
    
with d_col:
    st.image(img4, width=200)
    st.markdown('Julia Spina')
    
    st.image(img5, width=200)
    st.markdown('Luiz Ravache')
    
    st.image(img6, width=200)
    st.markdown('Otavio Messer')
   
# Texto introdutório
st.markdown("Criadores: Grupo 7 do segundo semestre da graduação de Engenharia Biomédica da Faculdade Israelita de Ciências da Saúde Albert Einstein: Antonio Elias Faiçal Júnior, Bianca Peixoto, Eduardo de Angelis Szikszay, Julia Rosa Spina, Luiz Gustavo Ravache de Oliveira, Otavio Nunes Ferreira Messer.")
