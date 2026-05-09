import pandas as pd
from datetime import datetime

print("Iniciando o pipeline de dados de Uberlândia...")

# 1. EXTRAÇÃO (Simulando a coleta de sensores na cidade)
dados_brutos = {
    'sensor_id': [101, 102, 103],
    'cidade': ['Uberlândia', 'Uberlândia', 'Uberlândia'],
    'temperatura_celsius': [28.5, 30.2, 25.4],
    'umidade_ar': [45, 40, 60],
    'data_coleta': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * 3
}

df = pd.DataFrame(dados_brutos)

# 2. TRANSFORMAÇÃO (Regra de negócio: converter Celsius para Fahrenheit)
df['temperatura_fahrenheit'] = (df['temperatura_celsius'] * 9/5) + 32

# 3. CARGA (Salvando o dado processado para análise futura)
df.to_csv('relatorio_clima_uberlandia.csv', index=False)

print("Pipeline finalizado! O arquivo 'relatorio_clima_uberlandia.csv' foi gerado.")
