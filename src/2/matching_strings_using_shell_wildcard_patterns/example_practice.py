# example.py
#
# Example of using shell-wildcard style matching in list comprehensions


from fnmatch import fnmatchcase as match

names = ['Dat1.csv', 'Dat2.csv','config.ini','foo.py']

a = [name for name in names if match(name, 'Dat*.csv')]

print(a)

#OS에 따라 fnmatch의 Case Sensitivity가 틀림, 막상해보니 windows에서도 case를 구분하는 거 같음. 
#OS X(mac)
fnmatch('foo.txt', '*.TXT')
#>>>False
#Windows
tf = match('foo.txt', '*.TXT')
print(tf)
# >>>True
# 위  같은 경우에는 CASE를 정확하게 구분하기 위해서는 fnmatchcase 사용
tf = match('foo.txt', '*.TXT')
print(tf)


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '54[0-9][0-9] *CLARK*')]
print(b)




