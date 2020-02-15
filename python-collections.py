# Created on Jul 26, 2013
# @author: tunatore

# python collections

# tuple example which is generally not mutable
animals = ('Cat', 'Dog', 'Elephant', 'Bird', 'Tiger', 'Lion', \
           'Rabbit')

# tuples are accessed by index and similar to list
print("this will print", animals[0])  # index starts from 0
print("this will print", animals[6])

# IndexError: tuple index out of range
# print (animals[7])

listAnimals = ['', 'Goose', 'Bison', 'Pelican']

# list access
print("list print", listAnimals[0])
print("list print", listAnimals[1])
print("list print", listAnimals[3])

# list difference, you can change lists
listAnimals.append('Whale')
print("list print", listAnimals[4])

# add Whale again to list
listAnimals.append('Whale')
print("list print", listAnimals[5])

# count Whale element in List

print("list Whale count is", listAnimals.count('Whale'))

# remove Whale element first occurrence
listAnimals.remove('Whale')

print("list Whale count is", listAnimals.count('Whale'))

# list total elements count
print("Count Elements in listAnimals", len(listAnimals))

# you can also count tuples with len
print("Count Elements in animals Tuple", len(animals))

# before list sort
print("before sort", listAnimals[1])
print("before sort", listAnimals[2])
print("before sort", listAnimals[3])

listAnimals.sort()

# after list sort
print("after sort", listAnimals[1])
print("after sort", listAnimals[2])
print("after sort", listAnimals[3])

# python dictionary example
dictionaryAnimalSpeed = {'tiger': 65, 'monkey': 25, 'bison': 35, 'cheetah': 113}

# accessing dictionary with key
print("monkey's speed -", dictionaryAnimalSpeed['monkey'])
print("tiger's speed -", dictionaryAnimalSpeed['tiger'])

# you can even change tiger's speed
dictionaryAnimalSpeed['tiger'] = 71
print("new tiger's speed -", dictionaryAnimalSpeed['tiger'])
# adding new element
dictionaryAnimalSpeed['cow'] = 25

# getting dictonary keys
animalNamesInDictionary = dictionaryAnimalSpeed.keys()
for animal in animalNamesInDictionary:
    print("animal name ", animal)

# ordered dictionary

import collections

print("\nordered dictionary")
orderedDictionary = collections.OrderedDict(sorted(dictionaryAnimalSpeed.items()))
for key, value in orderedDictionary.items():
    print(key, value)

# deque python

from collections import deque

q = deque([1, 2, 3, 4, 5, 6])

q.append(7)
q.append(8)

print("\ndeque:", q)

print("deque pop", q.pop())
print("deque popleft", q.popleft())

print("\ndeque:", q)

