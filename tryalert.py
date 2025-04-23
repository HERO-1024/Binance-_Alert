from binance.client import Client
import time

# Binance API credentials
API_KEY = 'YOUR API KEY'
client = Client(API_KEY)

# Symbols and their target prices
targets = {
    'BTCUSDT': 911150.8,
    'BNBUSDT': 612.60,
    'ETHUSDT': 1802.00,
    'SOLUSDT': 152.40
}

def check_price():
    while True:
        try:
            for symbol, target_price in targets.items():
                ticker = client.get_symbol_ticker(symbol=symbol)
                current_price = float(ticker['price'])

                print(f"Current {symbol} price: ${current_price:.2f}")

                if current_price >= target_price:
                    print(f"\n🚨 ALERT: {symbol} has reached your target price of ${target_price}!\n")
                    return  # Stop monitoring after any one hits target

        except Exception as e:
            print(f"[ERROR] {e}")
            print("Retrying...\n")

        time.sleep(10)  # Wait before checking again

if __name__ == "__main__":
    check_price()
