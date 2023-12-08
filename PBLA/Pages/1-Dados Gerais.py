import GLinha_Res_Tempo as GL
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header ('Dados Gerais') 

df = GL.grafLinha('C:/dados_PBL_nomebonitinho.xlsx',dias)

chart = alt.Chart(df).mark_line().encode(
    x='tempo',
    y='status',
    color='microorganismo',
)

st.altair_chart(chart, use_container_width=True)
