# example.py
#
# Some examples of using generators in arguments

# basic transforming

nums = [1,2,3,4,5]
s = sum(x * x for x in nums)
print(s)

#determin if any .py
import os
files = os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
mins_shares = min(x['shares'] for x in portfolio)
print(mins_shares)

#dictionary list의 key를 할용하는 경우, dictionary 항목이 필요한 경우
min_shares = min(portfolio, key=lambda s:s['shares'])
print("using key : ", min_shares)


# 데이터의 크기가 클경우 temporary list을 만들지 않고 사용하는 것이 memory-efficient함.
# temporary list를 사용하는 경우
s = sum([x*x for x in nums])
print("Temporary List created : ", s)

# temporary list를 사용자히 않고 generator expression을 사용하는 경우
s = sum(x*x for x in nums)