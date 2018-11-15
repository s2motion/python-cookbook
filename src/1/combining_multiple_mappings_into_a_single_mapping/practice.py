a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

#combining maps into a single map using Chain Map
#ChainMap 어느 버전에 있는지 모르겠지만 3.3.2에는 존재하지 않음.
from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])