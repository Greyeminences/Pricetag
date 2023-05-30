#!/usr/bin/env python3
price = 1000

try:
    price = int(input("How much do you love me in range 0 - 100: "))
except ValueError:
    print("Robert, you're dumb!")

# print(value)

# [0, 1, 2, ..., 10]
# elif price in list(range(10+1, 50+1))

if price <= 0:
    print(price, "that's so sad")
elif price > 0 and price <= 10:
    print(price, "it's a lot")
elif price > 10 and price <= 50:
    print(price, "it's even more")
elif price > 50 and price <= 99:
    print(price, "oh man")
else:
    print("woah, me too")

# :)
# Robert was there (:
# <3
