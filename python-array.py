import array as arr

int_array = arr.array('i', [1, 2, 3, 4, 5, 6])  # integer array

# array elements

print("first element", int_array[0])
print("last element", int_array[-1])

double_array = arr.array('d', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

# error double_array = arr.array('d', ["1.0", 2.0, 3.0, 4.0, 5.0, 6.0])

# change array elements

int_array[0] = 100
print(int_array)

int_array[2:5] = arr.array('i', [8, 8, 8])
print(int_array)

# array add elements

int_array.append(2)
print(int_array)

# array add several items

int_array.extend([1, 2, 3, 4, 5])
print(int_array)

# find element and delete
int_array.remove(100)
print(int_array)

# delete element by index
del int_array[0]
print(int_array)

int_array.pop(4)
print(int_array)

# slice arrays

print("int_array[2:3]", int_array[2:3])
print("int_array[0:5]", int_array[0:5])
print("int_array[:-5]", int_array[:-5])
print("int_array[5:]", int_array[5:])
print("int_array[-1]", int_array[-1])

# reverse array
print(int_array[::-1])