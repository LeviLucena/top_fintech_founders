import pandas as pd
import streamlit as st
import requests

st.set_page_config(page_title="Top Foundadores Fintech", layout="wide")

st.title("🚀 Fundadores Emergentes de Fintech no Brasil")

query = st.text_input("🔍 Filtro semântico (ex: 'pix open finance')", "fintech inovação")

if st.button("🔎 Buscar"):
    url = f"http://127.0.0.1:8000/top-founders?query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.success(f"🔝 Mostrando {len(df)} fundadores encontrados")
        st.dataframe(df.sort_values(by='score', ascending=False))

        st.bar_chart(df.set_index("name")["score"])
    else:
        st.error("Erro ao buscar dados da API.")
