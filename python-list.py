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

list += [1,2,3,4,5,6]
print(list)
