import yfinance as yf
import streamlit as st
import pandas as pd

# Define uma função para verificar a tendência do preço do petróleo
def verificar_tendencia_petroleo(ticker="CL=F"):
    dados = yf.download(ticker, period="1mo")
    if dados.empty:
        return False
    return dados['Close'][-1] > dados['Close'][0]

# Define uma função para obter dados das empresas petrolíferas
def obter_dados_empresas(empresas):
    dados_empresas = {}
    for nome, ticker in empresas.items():
        dados = yf.Ticker(ticker)
        ultimo_preco = dados.history(period="1d")['Close'].iloc[-1]
        dados_empresas[nome] = {'Ticker': ticker, 'Último Preço': ultimo_preco}
    return dados_empresas

# Lista de empresas petrolíferas e seus tickers
empresas_petroliferas = {
    "Petrobras": "PBR",
    "Exxon Mobil": "XOM",
    "Chevron": "CVX",
    "BP": "BP"
}

# Script Streamlit
st.title('Analisador de Tendência do Petróleo e Seleção de Ativos')

if st.button('Analisar Tendência do Petróleo e Selecionar Empresas Petrolíferas'):
    if verificar_tendencia_petroleo():
        st.write("Tendência de alta no preço do petróleo identificada.")
        dados_empresas = obter_dados_empresas(empresas_petroliferas)
        df = pd.DataFrame.from_dict(dados_empresas, orient='index')
        st.write(df)
    else:
        st.write("Nenhuma tendência de alta no preço do petróleo foi identificada. Considerar outras análises.")
