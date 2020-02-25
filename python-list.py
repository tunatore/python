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
print(list)

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
print("list.index(2):" , list.index(2))

print([list] * 2)

# list comprehension
square_list = [x * x for x in range(1, 5)]
print(square_list)

# list comprehension with condition
square_list_condition = [x * x for x in range(1,5) if x != 2 and x != 1]
print(square_list_condition)