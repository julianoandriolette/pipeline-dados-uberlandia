import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Dashboard Clima Uberlândia", page_icon="🌤️")

st.title("🌤️ Pipeline de Dados: Uberlândia - Juliano")
st.markdown(f"**Estudante:** Juliano Gomes | **Curso:** Sistemas de Informação (Uniessa)")

# 1. EXTRAÇÃO (Simulada)
dados_brutos = {
    'Sensor': ['Centro', 'Santa Mônica', 'Umuarama'],
    'Temp ºC': [28.5, 30.2, 25.4],
    'Umidade %': [45, 40, 60],
    'Última Atualização': [datetime.now().strftime("%d/%m/%Y %H:%M")] * 3
}

df = pd.DataFrame(dados_brutos)

# 2. TRANSFORMAÇÃO
df['Temp ºF'] = (df['Temp ºC'] * 9/5) + 32

# 3. VISUALIZAÇÃO (A "Carga" para o usuário)
st.subheader("Dados Processados do Pipeline")
st.table(df)

st.info("Este dashboard demonstra um processo de ETL (Extract, Transform, Load) rodando na nuvem.")
