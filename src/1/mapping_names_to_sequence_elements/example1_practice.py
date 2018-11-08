# example.py

from collections import namedtuple
# from pprint import pprint

Subscriber = namedtuple('Subscriber', ['addr','joined'])
sub = Subscriber('jonesy@example.com','1975-02-19')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr, joined = sub

print(addr)
print(joined)

#ordinary method
# def compute_cost(records):
# 	total = 0.0
# 	for record in records:
# 		total += record[1] * record[2]
# 	return total
# pprint(sub)

# using namedtuple 'Stock' record contains 'name', 'shares', 'price'
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
# calculate cost , cost = sum(shares*price) method compute_cost

def compute_cost(records):
	total = 0.0
	for record in records:
		s = Stock(*record)
		total += s.shares * s.price
	return total

# Some Data
records = [
    ('GOOG', 100, 490.1),
    ('ACME', 100, 123.45),
    ('IBM', 50, 91.15)
]

print(compute_cost(records))

#namedtuple is immutable
#if you want to change value then use _replace

s = Stock('ACME', 100, 123.45)
# s._shares = 200
# it causes errot because namedtuple is immutable
# use _replace
s = s._replace(shares=200)
print(s.shares)

# it can be a convenient way to populate name tuples that have optional or missing fields.
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

#create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

#function to convert a dictionary to a Stock
def dict_to_stock(s):
	return stock_prototype._replace(**s)


a = {'name':'ACME', 'shares':100, 'price':123.45}
print(dict_to_stock(a))

