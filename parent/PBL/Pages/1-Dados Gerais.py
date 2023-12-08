import uServ13 as GL
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import Main as M

st.header("Resistência Adquirida por Bactéria x Tempo")

uploaded_file = GL.grafLinha("C:/pbl/dados_PBL_nomebonitinho.xlsx")

if uploaded_file is not None:
    df = GL.grafLinha(uploaded_file)
    st.markdown("Upload com sucesso.")

    if type(df) == int:
        st.markdown("Não foi possível ler o arquivo.")
        exit()
    else:
        chart = alt.Chart(df).mark_line().encode(
            x='tempo',
            y='status',
            color='microorganismo',
        )

        # Display the chart using Streamlit
        st.altair_chart(chart, use_container_width=True)
