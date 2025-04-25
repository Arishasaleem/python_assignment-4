import streamlit as st

# Page Configuration
st.set_page_config(page_title="About Cryptocurrency", page_icon="💰")

# Title
st.title("About Cryptocurrency")

# Introduction
st.write("""
Cryptocurrency is a digital or virtual form of money that uses cryptography for security.
Unlike traditional currencies issued by governments, cryptocurrencies operate on decentralized networks based on blockchain technology.
""")

# How Cryptocurrency Works
st.header("How Cryptocurrency Works")
st.write("""
Cryptocurrencies function using blockchain technology, a distributed ledger that records transactions securely and transparently.
""")

st.markdown("**Key Features:**")
st.markdown("- **Decentralization**: No central authority controls cryptocurrencies.")
st.markdown("- **Security**: Transactions are secured through cryptographic techniques.")
st.markdown("- **Anonymity**: Users can make transactions without revealing their identities.")
st.markdown("- **Borderless Transactions**: Cryptocurrencies can be sent and received globally.")

# Popular Cryptocurrencies
st.header("Popular Cryptocurrencies")
st.write("Some of the well-known cryptocurrencies include:")
st.markdown("- **Bitcoin (BTC)**: The first and most widely known cryptocurrency.")
st.markdown("- **Ethereum (ETH)**: Known for its smart contract functionality.")
st.markdown("- **Binance Coin (BNB)**: Used within the Binance ecosystem.")
st.markdown("- **Ripple (XRP)**: Focused on fast and low-cost cross-border payments.")

# Benefits & Risks
st.header("Benefits & Risks")
st.write("""
### Benefits:
- Lower transaction fees compared to traditional banking.
- Fast international transactions.
- Provides financial access to unbanked populations.
- Investment opportunities in a growing market.

### Risks:
- **Volatility**: Prices can fluctuate dramatically.
- **Regulatory Issues**: Government policies may impact cryptocurrency use.
- **Security Threats**: Risks of hacking and fraud.
""")

# Conclusion
st.header("Conclusion")
st.write("""
Cryptocurrency is changing the financial world with decentralization and security.
Stay informed, invest wisely, and explore the future of digital finance!
""")
