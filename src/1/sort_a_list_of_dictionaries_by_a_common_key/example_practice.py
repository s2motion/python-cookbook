# example.py
#
# Sort a list of a dicts on a common key

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
#using itemgetter
from operator import itemgetter

# sorting rows_by_fname
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# sorting rows_by_uid
rows_by_uid = sorted(rows, key=itemgetter('uid'))

from pprint import pprint
print("Sorted by fname:")
#print(rows_by_fname)
pprint(rows_by_fname)

print("Sorted by uid:")
pprint(rows_by_uid)

# itemgetter lambda로 대신할 수 있으나 itemgetter가 좀더 빠름...
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
pprint(rows_by_fname)

# sorting rows_by_lfname with multiple keys (lname, fname)
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print("Sorted by lname,fname:")
pprint(rows_by_lfname)
