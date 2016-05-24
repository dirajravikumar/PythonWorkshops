items = -1
total = 0

while items < 0:
    items = int(input("Enter number of item(s)"))
for i in range(items):
    price = int(input("Enter the price of item(s) $"))
    total = total + price

if total > 100:
    print("The total shipping cost is $", total - total/10)
else:
    print("The total shipping cost is $", total)
