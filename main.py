import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página com tema Dark/Neon
st.set_page_config(page_title="Pipeline JA.data", page_icon="🧪", layout="wide")

# CSS para injetar o estilo Neon no Streamlit
st.markdown("""
    <style>
    .main { background-color: #020508; color: #ffffff; }
    .stMetric { background-color: #060c12; border: 1px solid #00ffff; padding: 15px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,255,255,0.2); }
    h1 { color: #00ffff; text-shadow: 0 0 10px #00ffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 Pipeline de Dados | Uberlândia - MG")
st.write(f"**Engenheiro responsável:** Juliano Andriolette")

# Simulação de Extração (ETL)
st.subheader("1. Extração e Transformação")
data = {
    'Localidade': ['Centro', 'Santa Mônica', 'Umuarama', 'Granja Marileusa'],
    'Temperatura (ºC)': [28.4, 30.1, 27.5, 29.8],
    'Umidade (%)': [45, 42, 50, 44],
    'Status': ['Ativo', 'Ativo', 'Ativo', 'Ativo']
}
df = pd.DataFrame(data)

# Métricas em destaque
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura Média", f"{df['Temperatura (ºC)'].mean():.1f} °C")
col2.metric("Umidade Média", f"{df['Umidade (%)'].mean():.0f}%")
col3.metric("Sensores Ativos", "4/4")

# Exibição da Tabela Processada
st.subheader("2. Carga (Dados Processados)")
st.dataframe(df.style.highlight_max(axis=0, color='#004444'))

st.info("Pipeline integrado via GitHub e hospedado na Streamlit Cloud.")
