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