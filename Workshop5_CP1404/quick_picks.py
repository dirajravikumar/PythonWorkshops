import random

num_picks = int(input("How many quick picks? "))

total = 1
for n in range(1, num_picks + 1):
    print("{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(random.randint(1, 46), random.randint(1, 46), random.randint(1, 46), random.randint(1, 46), random.randint(1, 46), random.randint(1, 46)))
    total += 1
    total == num_picks
