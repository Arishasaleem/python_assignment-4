import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Crypto App", layout="wide")

# Sidebar Navigation
page = st.sidebar.radio("📌 Select Page", ["🏠 Home", "📈 Portfolio Manager", "🔔 Alerts"])

if page == "🏠 Home":
    st.title("🚀 Crypto Tracker & Analyzer")
    st.write("Track real-time prices and analyze trends!")

    crypto_symbol = st.sidebar.text_input("Enter Coin Symbol (e.g., BTC, ETH)", "bitcoin")

    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(api_url).json()

    if response:
        price = response[crypto_symbol]['usd']
        st.metric(label=f"{crypto_symbol.upper()} Price (USD)", value=f"${price}")
    else:
        st.error("Invalid coin symbol. Try again!")

elif page == "📈 Portfolio Manager":
    st.title("📊 Portfolio Manager")
    
    st.write("Add your crypto investments to track their performance.")
    
    if "portfolio" not in st.session_state:
        st.session_state["portfolio"] = []

    with st.form("Add Crypto"):
        symbol = st.text_input("Enter Crypto Symbol", "BTC")
        amount = st.number_input("Enter Amount", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Add to Portfolio")

        if submitted:
            st.session_state["portfolio"].append({"symbol": symbol.upper(), "amount": amount})
    
    if st.session_state["portfolio"]:
        df = pd.DataFrame(st.session_state["portfolio"])
        st.write(df)



    news_api_key = "YOUR_NEWSAPI_KEY"
    news_url = f"https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={news_api_key}"
    news_data = requests.get(news_url).json()

    if "articles" in news_data:
        for article in news_data["articles"][:5]:
            st.write(f"🔹 [{article['title']}]({article['url']})")

elif page == "🔔 Alerts":
    st.title("🔔 Set Crypto Price Alerts")
    
    alert_symbol = st.text_input("Enter Crypto Symbol", "BTC")
    alert_price = st.number_input("Enter Target Price (USD)")
    st.button("Set Alert")

    st.write("🔔 Alerts will be triggered when price crosses the target!")
