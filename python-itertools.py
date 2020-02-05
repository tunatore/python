'''
Created on Aug 3, 2013

@author: tunatore
'''

# python itertools examples
# Functions creating iterators for efficient looping
# refer to http://python.readthedocs.org/en/v2.7.2/library/itertools.html

from itertools import *

# count
# counter starting from 1 to infinite
for i in count(1):
    print(i, " ", end="")
    if (i == 15):
        break
    # 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
print("\n")

# counter starting from 1 (increment with 5) to infinite
for i in count(1, 5):
    print(i, " ", end="")
    if (i >= 50):
        break
    # 1  6  11  16  21  26  31  36  41  46  51

print("\n")

# cycle
c = cycle("TUNA")
for i in range(12):
    print(next(c), end="")

# TUNATUNATUNATUNATUNATUNA

print("\n")

# repeat
for i in repeat('python', 4):
    print(i, end="")

# pythonpythonpythonpython

# chain
print("\n")
list1 = ['Test1', 'Goose', 'Bison', 'Pelican']
list2 = ['Cat', 'Dog', 'Elephant', 'Bird', 'Tiger', 'Lion', 'Rabbit']
print([i for i in chain(list1, list2)], "\n")
# ['Test1', 'Goose', 'Bison', 'Pelican', 'Cat', 'Dog', 'Elephant', 'Bird', 'Tiger', 'Lion', 'Rabbit']

# compress
print([i for i in compress('TUNATORE', [1, 1, 1, 1, False, False, False, 0])], "\n")
# ['T', 'U', 'N', 'A']
# or
print([i for i in compress('TUNATORE', [0, 0, 0, 0, 1, 1, 1, 1])], "\n")
# ['T', 'O', 'R', 'E']

# dropwhile (starts when prediction fails)
print([i for i in dropwhile(lambda z: z > 3, [9, 5, 6, 7, 2, 1, 4, 5, 6])], "\n")
# [2, 1, 4, 5, 6]

# takewhile (starts when as long as prediction true)
print([i for i in takewhile(lambda z: z > 6, [9, 8, 7, 6, 5, 4, 3, 2, 1])], "\n")
# [9, 8, 7]

# filterfalse (z>3 false items will return)
print([i for i in filterfalse(lambda z: z > 3, [9, 5, 6, 7, 2, 1, 4, 5, 6])], "\n")
# [2, 1]
# or
# filterfalse (z>3 false items will return)
print([i for i in filterfalse(lambda z: z < 3, [9, 5, 6, 7, 2, 1, 4, 5, 6])], "\n")
# [9, 5, 6, 7, 4, 5, 6]

# isslice
print([i for i in islice('tuna', 2)], "\n")
# ['t', 'u']
print([i for i in islice('tuna', 2, 3)], "\n")
# ['n']
print([i for i in islice('tuna', 0, None)], "\n")
# ['t', 'u', 'n', 'a']

# zip_longest
print([i for i in zip_longest('tntr', 'uaoe', fillvalue='')], "\n")
# [('t', 'u'), ('n', 'a'), ('t', 'o'), ('r', 'e')]

# product for cartesian
print([i for i in product('tuna', 'tore')], "\n")
# [('t', 't'), ('t', 'o'), ('t', 'r'), ('t', 'e'), ('u', 't'), ('u', 'o'), ('u', 'r'), ('u', 'e'), ('n', 't'),
# ('n', 'o'), ('n', 'r'), ('n', 'e'), ('a', 't'), ('a', 'o'), ('a', 'r'), ('a', 'e')]

# permutations
print([i for i in permutations('tuna', 4)], "\n")
# [('t', 'u', 'n', 'a'), ('t', 'u', 'a', 'n'), ('t', 'n', 'u', 'a'), ('t', 'n', 'a', 'u'), ('t', 'a', 'u', 'n'),
# ('t', 'a', 'n', 'u'), ('u', 't', 'n', 'a'), ('u', 't', 'a', 'n'), ('u', 'n', 't', 'a'), ('u', 'n', 'a', 't'),
# ('u', 'a', 't', 'n'), ('u', 'a', 'n', 't'), ('n', 't', 'u', 'a'), ('n', 't', 'a', 'u'), ('n', 'u', 't', 'a'),
# ('n', 'u', 'a', 't'), ('n', 'a', 't', 'u'), ('n', 'a', 'u', 't'), ('a', 't', 'u', 'n'), ('a', 't', 'n', 'u'),
# ('a', 'u', 't', 'n'), ('a', 'u', 'n', 't'), ('a', 'n', 't', 'u'), ('a', 'n', 'u', 't')]

# groupby
# useful itemgetter import
from operator import itemgetter

salesByDay = [('20130101', 35), ('20130101', 25), ('20130102', 35), ('20130101', 40), ('20130103', 66),
              ('20130103', 66), ('20130102', 44)]

# keys have to be sorted
sortedSalesByDay = sorted(salesByDay, key=itemgetter(0))
for key, values in groupby(sortedSalesByDay, itemgetter(0)):
    print("Day:", key)
    for value in values:
        print("Value ", value[1])

# Day: 20130101
# Value  35
# Value  25
# Value  40
# Day: 20130102
# Value  35
# Value  44
# Day: 20130103
# Value  66
# Value  66
