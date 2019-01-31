# example.py
#
# Examples of simple regular expression matching

# Exact Match & Match at start or end & Search for the location of the first occurence
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact Match
print(text == 'yeah')
# >>>False

# Match at start or end
print(text.startswith('yeah'))
# >>>True
print(text.endswith('no'))
# >>>False

#Search for the location of the first occurences
print(text.find('no'))
# >>>10


import re

# Some sample text
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# # (a) Find all matching dates
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))
# # (b) Find all matching dates with capture groups. convert 2012-11-27
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
  print('{}-{}-{}'.format(year, month, day))

# # (c) Iterative search
for m in datepat.finditer(text):
  print(m.groups())
