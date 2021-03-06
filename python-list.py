list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.insert(5, 5)
list.append(10)
list.append(9)
list.append(6)

print(list)
list.sort()
print(list)

list.remove(3)
print(list)

pop = list.pop(2)
print(pop)
print(list)

list.reverse()
print("list.reverse()", list)
print("reversed(list)", list)

print(list.index(10))

list += [1, 2, 3, 4, 5, 6]
print("list", list)

# first element
print("first element:", list[0])
print("remainder of the list:", list[1:])

# list last element
print("list last element:", list[-1])

# first 2 elements
print("first 2 elements:", list[:2])

# last 2 elements
print("last 2 elements:", list[-2:])

# list insert element
print(list[:2] + [222] + list[-10:])

# char list
text = 'test'
print(text[0])

print(list)
print("list.index(2):", list.index(2))

print([list] * 2)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
list[0:4] = [6, 2, 5, 6]
print(list)

# list comprehension
square_list = [x * x for x in range(1, 5)]
print(square_list)

# list comprehension with condition
square_list_condition = [x * x for x in range(1, 5) if x != 2 and x != 1]
print(square_list_condition)

print([1, 2, 3, 2, 4, 5, 6].count(2))

# list comprehension
# [expression for item in iterable]
# [expression for item in iterable if condition]

a = [y for y in range(1, 10) if y % 2 == 0]
print(a)

b = [i * 2 for i in range(1, 10)]
print(b)

list = ["test1", "test2", "test3"]

for item in enumerate(list):
    print(item)

for index, item in enumerate(list):
    print("index:", index, "item:", item)

for index, item in enumerate(list, 100):
    print("index:", index, "item:", item)

iterator = iter(list)
i = 0
while i < len(list):
    i += 1
    print("iterator", next(iterator))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list1.extend(list2)
print(list1)

# list initialize
list_values = [None] * 10
print(list_values)

# list sort
list = ["A", "b", "E", "d", "a", "b"]
print(sorted(list, key=lambda x: x.lower()))
print(sorted(list, reverse=True))

# bisect

from bisect import bisect

list = [-3, -2, - 1, 0, 1, 2, 3, 4, 5, 6, 7]
# binary search
print(bisect(list, 6))

list = ["A", "b", "E", "d", "a", "b"]
print("".join(list))

# rotate array
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(arr[n:] + arr[0:n])

n = 3
print(arr[n:] + arr[0:n])
