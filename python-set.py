set_of_integers = set()
set_of_integers.add(1)
set_of_integers.add(1)
set_of_integers.add(2)
set_of_integers.add(3)
set_of_integers.add(4)
set_of_integers.add(5)

print("set of integers", set_of_integers)

set_of_integers2 = {1, 2, 2, 3, 4, 5, 6, 7, 8}
print("set of integers 2", set_of_integers2)

print("intersection", set_of_integers.intersection(set_of_integers2))
print("union", set_of_integers.union(set_of_integers2))

print("set of integers", set_of_integers2)
# set_of_integers2.remove(1) #same as discard but throws exception
set_of_integers2.discard(1)
print("set of integers after remove", set_of_integers2)

# intersection
intersection_numbers = set_of_integers & set_of_integers2
print("set_of_integers", set_of_integers)
print("set_of_integers2", set_of_integers2)
print("intersection", intersection_numbers)
all_numbers = set_of_integers | set_of_integers2
print("union", all_numbers)

difference_sets = set_of_integers2 - set_of_integers
print("difference_sets", difference_sets)

set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2}

#compare sets
print(set1 == set2)
print(set2 == set3)
print(set2 >= set3)