import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página - Clean Professional
st.set_page_config(page_title="JA.data Dashboard", page_icon="📊", layout="wide")

# CSS para remover cores fortes e brilhos (Sombras e bordas suaves)
st.markdown("""
    <style>
    /* Fundo Dark suave e elegante */
    .stApp { 
        background-color: #11141d; 
        color: #cfd8dc; 
    }
    
    /* Cards de métricas: Sem brilho forte, bordas discretas */
    [data-testid="stMetric"] {
        background-color: #1a1f2b;
        border: 1px solid #333c4d;
        padding: 20px;
        border-radius: 12px;
        box-shadow: none;
    }
    
    /* Títulos em tom de Azul Acinzentado (Slate) sem brilho */
    h1, h2, h3 { 
        color: #90a4ae !important; 
        font-weight: 600 !important;
        text-shadow: none !important;
    }
    
    /* Labels das métricas mais suaves */
    [data-testid="stMetricLabel"] {
        color: #78909c !important;
    }
    
    /* Valor numérico da métrica */
    [data-testid="stMetricValue"] {
        color: #eceff1 !important;
    }

    /* Ajuste de links e info */
    .stAlert {
        background-color: #1a1f2b;
        border: 1px solid #333c4d;
        color: #90a4ae;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Pipeline de Dados | Uberlândia - MG")
st.write(f"Gestão Técnica: Juliano Andriolette")

# Simulação de ETL
st.subheader("Processamento de Fluxo")
data = {
    'Localidade': ['Centro', 'Santa Mônica', 'Umuarama', 'Granja Marileusa'],
    'Temperatura (ºC)': [28.4, 30.1, 27.5, 29.8],
    'Umidade (%)': [45, 42, 50, 44],
    'Status': ['Estável', 'Estável', 'Estável', 'Estável']
}
df = pd.DataFrame(data)

# Métricas com visual limpo
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura Média", f"{df['Temperatura (ºC)'].mean():.1f} °C")
col2.metric("Umidade Média", f"{df['Umidade (%)'].mean():.0f}%")
col3.metric("Status do Sistema", "Online")

# Tabela com cores neutras
st.subheader("Dados Consolidados")
st.dataframe(df, use_container_width=True)

st.info("Visual otimizado para análise técnica. Integração contínua via GitHub.")
