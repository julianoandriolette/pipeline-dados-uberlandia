import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# 1. Configuração da Página (OBRIGATORIAMENTE O PRIMEIRO COMANDO STREAMLIT)
st.set_page_config(page_title="JulianoAndriolette | Dashboard Real-Time", page_icon="🌐", layout="wide")

# 2. Configuração de Cache (Melhora a performance e economiza sua API)
@st.cache_data(ttl=3600)  # Atualiza os dados a cada 1 hora
@st.cache_data(ttl=3600)
def get_weather_data():
    url = "https://api.hgbrasil.com/weather?woeid=455913&key=79822a63"
    
    # Adicionando um User-Agent para evitar que a API bloqueie o Python
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # Se der erro de falta de autorização ou limite (ex: 403, 429)
        if response.status_code != 200:
            st.warning(f"Status da API: {response.status_code} - {response.text}")
            return None
            
        return response.json()['results']
    except Exception as e:
        st.error(f"Erro de Conexão: {e}")
        return None

# Estilo Clean Dark
st.markdown("""
    <style>
    .stApp { background-color: #11141d; color: #cfd8dc; }
    [data-testid="stMetric"] {
        background-color: #1a1f2b;
        border: 1px solid #333c4d;
        padding: 20px;
        border-radius: 12px;
    }
    h1, h2, h3 { color: #90a4ae !important; font-weight: 600; }
    .stChart { background-color: #1a1f2b; padding: 10px; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica de Saudação Dinâmica
hora_atual = datetime.now().hour
if 5 <= hora_atual < 12:
    saudacao = "Bom dia"
elif 12 <= hora_atual < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

st.title(f"🌐 {saudacao}, Juliano!")
st.write("Monitoramento de dados climáticos em tempo real para Uberlândia, MG")

data = get_weather_data()

if data:
    # Métricas Principais
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperatura Atual", f"{data['temp']}°C")
    col2.metric("Umidade", f"{data['humidity']}%")
    col3.metric("Vento", data['wind_speedy'])
    col4.metric("Condição", data['description'])

    # Organizando os dados de previsão
    forecast_df = pd.DataFrame(data['forecast'])
    
    # 4. Gráfico de Tendência de Temperatura
    st.subheader("📈 Tendência de Temperatura (Próximos Dias)")
    
    # Preparando dados para o gráfico de forma explícita
    chart_data = forecast_df[['date', 'max', 'min']].set_index('date')
    
    # Mapeamento de cores seguro para as colunas do Streamlit
    st.line_chart(chart_data, y=["max", "min"], color=["#ff4b4b", "#0077ff"]) 

    # Tabela Detalhada
    st.subheader("📋 Detalhamento da Previsão")
    clean_df = forecast_df[['date', 'weekday', 'max', 'min', 'description']].copy()
    clean_df.columns = ['Data', 'Dia', 'Máx (°C)', 'Min (°C)', 'Condição']
    st.dataframe(clean_df, use_container_width=True, hide_index=True)

else:
    st.error("Erro ao conectar com a API. Verifique sua conexão ou limite de requisições.")

st.info("Pipeline Otimizado: API -> Cache (1h) -> Pandas -> Gráficos Dinâmicos -> Streamlit Cloud")
