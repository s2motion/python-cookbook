# example.py
#
# Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min_price : ', min_price)
print('max_price : ', max_price)

#sorted
price_sorted = sorted(zip(prices.values(), prices.keys()))

for price, name in price_sorted:
  print('     ', name, price)

#discussiion
#dictionary의 min, max는 key에 적용됨
print(min(prices))
print(max(prices))
#dictionary의 values의 min, max prices.values()를 사용
print(min(prices.values()))
print(max(prices.values()))
#dictionary의 values min, max에 대응되는 key를 찾기 위해서는 lambda 사용 
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

#값을 가져올려면 lookup 단계가 한번 더 있어야함.
print(prices[min(prices, key=lambda k: prices[k])])
print(prices[max(prices, key=lambda k: prices[k])])

#값이 동일할 경우 min/max는 key min/max를 활용 
prices = {'AAA':45.23, 'ZZZ':45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))