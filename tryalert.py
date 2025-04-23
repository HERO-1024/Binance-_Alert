from binance.client import Client
import time

# Binance API credentials
API_KEY = 'YOUR API KEY'
client = Client(API_KEY)

# List of symbols to monitor
symbols = ['BTCUSDT', 'BNBUSDT', 'ETHUSDT', 'SOLUSDT']

# Ask user to input target prices
targets = {}
print("🔧 Set your target prices for each symbol:")

for symbol in symbols:
    while True:
        try:
            user_input = input(f"Enter target price for {symbol}: ")
            targets[symbol] = float(user_input)
            break
        except ValueError:
            print("⚠️ Please enter a valid number.")
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
