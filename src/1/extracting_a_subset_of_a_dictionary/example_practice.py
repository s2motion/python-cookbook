# example of extracting a subset from a dictionary
from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}

print("All prices over 200")
pprint(p1)

# same abole 위에 comprehension으로 한게 더 빠르고 표현이 명확함.
# p1 = dict((key, value) for key, value in prices.items() if value > 200)

# print("All prices over 200 by dict function")
# print(p1)

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }

p2 = {key:value for key, value in prices.items() if key in tech_names}
print("All techs")
pprint(p2)

# 다른 방법 하지만 위 방법보다 느림.
# p2 = {key:prices[key] for key in prices.keys() & tech_names}
# print("All techs by & ")
# pprint(p2)


