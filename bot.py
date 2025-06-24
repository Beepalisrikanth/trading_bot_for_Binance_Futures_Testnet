import os
import time
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
import logging

# Load env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        print("[+] Connected to Binance Futures Testnet")

    def get_server_timestamp(self):
        """Always get a fresh server timestamp"""
        server_time = self.client.futures_time()['serverTime']
        return server_time

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity,
                timestamp=self.get_server_timestamp(),
                recvWindow=5000
            )
            logging.info(f"Market order: {order}")
            print("Market Order:", order)
        except Exception as e:
            logging.error(f"Market order error: {str(e)}")
            print("Error:", e)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
                timestamp=self.get_server_timestamp(),
                recvWindow=5000
            )
            logging.info(f"Limit order: {order}")
            print("Limit Order:", order)
        except Exception as e:
            logging.error(f"Limit order error: {str(e)}")
            print("Error:", e)

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    while True:
        print("\n==== Binance Futures Trading Bot ====")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            bot.place_market_order(symbol, side, qty)

        elif choice == "2":
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            price = input("Price: ")
            bot.place_limit_order(symbol, side, qty, price)

        elif choice == "3":
            print("Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
