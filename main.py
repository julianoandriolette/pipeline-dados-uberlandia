import streamlit as st
import pandas as pd
import requests

# Configuração Clean Dark
st.set_page_config(page_title="JA.data | Real-Time", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #11141d; color: #cfd8dc; }
    [data-testid="stMetric"] {
        background-color: #1a1f2b;
        border: 1px solid #333c4d;
        padding: 20px;
        border-radius: 12px;
    }
    h1, h2, h3 { color: #90a4ae !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Pipeline de Dados Real-Time")
st.write("Dados extraídos via API HG Brasil para Uberlândia, MG")

# Função para buscar dados da API
def get_weather_data():
    # Usando woeid de Uberlândia: 455913
    url = "https://api.hgbrasil.com/weather?woeid=455913&key=79822a63"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return None

data = get_weather_data()

if data:
    # Métricas Reais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperatura Atual", f"{data['temp']}°C")
    col2.metric("Umidade", f"{data['humidity']}%")
    col3.metric("Vento", data['wind_speedy'])
    col4.metric("Condição", data['description'])

    # Tabela de Previsão (Transformação de dados)
    st.subheader("Previsão para os próximos dias")
    forecast_df = pd.DataFrame(data['forecast'])
    
    # Selecionando e renomeando colunas para o dashboard
    clean_df = forecast_df[['date', 'weekday', 'max', 'min', 'description']].copy()
    clean_df.columns = ['Data', 'Dia', 'Máx (°C)', 'Min (°C)', 'Condição']
    
    st.dataframe(clean_df, use_container_width=True)
else:
    st.error("Erro ao conectar com a API. Verifique sua chave ou limite de requisições.")

st.info("Pipeline: API -> Python/Requests -> Pandas -> Streamlit Cloud")
