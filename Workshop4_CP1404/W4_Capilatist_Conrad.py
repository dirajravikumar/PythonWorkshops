import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

def format_currency(price):
    currency = print("${:,.2f}".format(price))
    return currency

price = INITIAL_PRICE
day = 0
print("Starting price: {}".format(format_currency(price)))

while price >= MIN_PRICE and price <= MAX_PRICE:
   priceChange = 0
   # generate a random integer of 1 or 2
   # if it's 1, the price increases, otherwise it decreases
   if random.randint(1, 2) == 1:
       # generate a random floating-point number
       # between 0 and MAX_INCREASE
       priceChange = random.uniform(0, MAX_INCREASE)
       day += 1
   else:
       # generate a random floating-point number
       # between negative MAX_INCREASE and 0
       priceChange = random.uniform(-MAX_DECREASE, 0)

   price *= (1 + priceChange)
   print("On day {} price is {}".format(day, format_currency(price)))

