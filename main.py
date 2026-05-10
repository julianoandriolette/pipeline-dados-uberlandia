import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página com tema Soft Dark
st.set_page_config(page_title="Pipeline JA.data", page_icon="🧪", layout="wide")

# CSS para injetar o estilo de cores suaves no Streamlit
st.markdown("""
    <style>
    /* Fundo azul marinho muito escuro conforme o portfólio */
    .main { 
        background-color: #0f111a; 
        color: #e1e2e1; 
    }
    /* Cards de métricas com bordas Lavanda Suave */
    [data-testid="stMetric"] {
        background-color: #191c29;
        border: 1px solid #b39ddb;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(179, 157, 219, 0.2);
    }
    /* Títulos em Lavanda com brilho sutil */
    h1, h2, h3 { 
        color: #b39ddb !important; 
        text-shadow: 0 0 8px rgba(179, 157, 219, 0.3); 
    }
    /* Estilo para labels de métricas */
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 Pipeline de Dados | Uberlândia - MG")
st.write(f"**Engenheiro responsável:** Juliano Andriolette")

# Simulação de Extração (ETL)
st.subheader("1. Processamento de Dados")
data = {
    'Localidade': ['Centro', 'Santa Mônica', 'Umuarama', 'Granja Marileusa'],
    'Temperatura (ºC)': [28.4, 30.1, 27.5, 29.8],
    'Umidade (%)': [45, 42, 50, 44],
    'Status': ['Ativo', 'Ativo', 'Ativo', 'Ativo']
}
df = pd.DataFrame(data)

# Métricas em destaque (Cores Azul Céu e Lavanda)
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura Média", f"{df['Temperatura (ºC)'].mean():.1f} °C")
col2.metric("Umidade Média", f"{df['Umidade (%)'].mean():.0f}%")
col3.metric("Sensores Operacionais", "4/4")

# Exibição da Tabela Processada (Estilo Menta Suave)
st.subheader("2. Dados Consolidados")
st.dataframe(df.style.highlight_max(axis=0, color='#2e3c30')) # Realce em tom de menta escuro

st.info("Pipeline JA.data: Processamento em tempo real via Streamlit Cloud.")
