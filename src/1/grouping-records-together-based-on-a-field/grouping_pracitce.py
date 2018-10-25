rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# first sorting, sort by date
from operator import itemgetter
from itertools import groupby
from pprint import pprint

rows.sort(key=itemgetter('date'))

pprint(rows);

# group by date and print date, items
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print('     ', item)

# using defaultdict
# sorting 없이 크기가 큰 데이터 구조에서 random access를 하려면 defaultdict을 사용 
# memory 문제가 없다면 groupby처럼 sorting을 먼저 할필요 없고 속도도 빠름.
# using default dict
from collections import defaultdict
print('############# using default dict')
rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)

# print the dictionary with the specific date ex)'07/02/2012'
print(rows_by_date['07/02/2012'])


