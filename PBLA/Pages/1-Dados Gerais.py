import uServ13 as GL
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header("tempo x res")

uploaded_file = st.file_uploader('Upload dos dados')
if uploaded_file is not None:
    df = GL.grafLinha( uploaded_file)
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
