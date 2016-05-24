import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
   priceChange = 0
   if random.randint(1, 2) == 1:
       priceChange = random.uniform(0, MAX_INCREASE)
   else:
       priceChange = random.uniform(-MAX_DECREASE, 0)

   price *= (1 + priceChange)
   print("${:,.2f}".format(price))