# example.py
#
# Example of splitting a string on multiple delimiters using a regex

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# (a) Splitting on space, comma, and semicolon
parts = re.split(r'[;,\s]\s*', line)
print(parts)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# (b) Splitting with a capture group
# ()을 정규표현식에 사용할 경우 delimeter를 포함한 group 형태로 분리됨.
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# (c) Rebuilding a string using fields above
values = fields[::2]
delimiters = fields[1::2]
delimiters.append('')
print('value =', values)
#value = ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print('delimiters =', delimiters)
#delimiters = [' ', ';', ',', ',', ',', '']

newline = ''.join(v+d for v, d in zip(values, delimiters))
print('newline =', newline)
#newline = asdf fjdk;afed,fjek,asdf,foo

# # (d) Splitting using a non-capture group
# delimeter를 포함하지  않는 방법은 ?:을 추가
parts = re.split(r'(?:;|,|\s)\s*', line)
print(parts)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']