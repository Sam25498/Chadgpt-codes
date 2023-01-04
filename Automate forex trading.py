from forex_python.converter import CurrencyRates

c = CurrencyRates()
price = c.get_rate('USD', 'EUR')
print(price)
