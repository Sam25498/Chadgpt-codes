from forex_python.converter import CurrencyRates

c = CurrencyRates()
price = c.get_rate('USD', 'EUR')
print(price)
import time

while True:
    # Retrieve the current price
    price = c.get_rate('USD', 'EUR')
    print(f'Current price: {price}')

    # Add your trading logic here

    # Sleep for 4 hours
    time.sleep(4 * 3600)
