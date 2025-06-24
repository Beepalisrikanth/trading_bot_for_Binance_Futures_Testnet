# 📈 Binance Futures Trading Bot

This is a **Python-based crypto trading bot** built for the **Binance USDT-M Futures Testnet**.  
It allows you to place **Market** and **Limit** orders directly from your command line, with robust logging and error handling.

---

## 🚀 **Features**

✅ Place **Market Orders** (BUY/SELL)  
✅ Place **Limit Orders** (BUY/SELL)  
✅ Uses official [python-binance](https://github.com/sammchardy/python-binance) library  
✅ Logs all requests, responses, and errors to `log.txt`  
✅ Supports clear user input via **Command-Line Interface (CLI)**  
✅ Uses secure API key management via `.env`

---

## ⚙️ **How to Setup**

### 1️⃣ Clone or download the repo

bash
git clone https://github.com/YOUR_USERNAME/trading-bot.git
cd trading-bot

2️⃣ Install dependencies
Create a virtual environment (optional but recommended):
python -m venv .venv
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

3️⃣ Configure your Binance Testnet API keys
Register for a Binance USDT-M Futures Testnet account:
 https://testnet.binancefuture.com

Generate your API Key and API Secret under API Management.
Create a .env file in your project root, using .env.example as a guide:

=======.env========
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_API_SECRET

====== How to Run========
python bot.py
Then follow the interactive menu:


==== Binance Futures Trading Bot ====
1. Place Market Order
2. Place Limit Order
3. Exit


![Image](https://github.com/user-attachments/assets/dca59646-3345-48f5-8f37-ba8c984a1a65)

![Image](https://github.com/user-attachments/assets/e0537ec2-4121-4e0c-8e87-142f034728aa)

