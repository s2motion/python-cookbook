# example.py
#
# Determine the most common words in a list

words = [
   'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
   'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
   'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
   'my', 'eyes', "you're", 'under'
]

from collections import Counter
words_count = Counter(words)
top_three = words_count.most_common(3)
print(top_three)
# top_three
# outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Example of merging in more words
morewords = ['why','are','you','not','looking','in','my','eyes']
words_count.update(morewords)
top_three = words_count.most_common(3)
print(top_three)
# outputs [('eyes', 9), ('the', 5), ('look', 4)]

#using dictionary that maps occurrences
print(words_count['not'])
# outputs 2
print(words_count['eye'])
# outputs 0

#increase the count manually or use update()
for words_any in morewords:
  words_count[words_any] += 1

print(words_count['eyes'])
#output 10

#combine, substact countesrs
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
print(a+b)
print(a-b)



