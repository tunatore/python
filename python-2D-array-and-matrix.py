# 2D array
# contains different number of elements in each array

twoDArray = [[1, 2, 3], [1], [1, 2], [1, 2, 3, 4]]
print("twoDArray", twoDArray)
print("twoDArray[0]", twoDArray[0])
print("twoDArray[1]", twoDArray[1])
twoDArray.insert(2, [1, 2, 3, 5, 5, 6])
print("twoDArray", twoDArray)

for arr in twoDArray:
    for element in arr:
        print(element, end=" ")
    print()

print()

for i in range(len(twoDArray)):
    for j in range(len(twoDArray[i])):
        print(twoDArray[i][j], end=" ")
    print()

# delete array in 2D array
del twoDArray[2]
print("twoDArray", twoDArray)

# matrix
# contains same number of elements in each array

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:", matrix)
print("matrix[0]:", matrix[0])
print("matrix[0][0]:", matrix[0][0])
print("matrix[0][1]:", matrix[0][1])
print("matrix[0][-1]:", matrix[0][-1])  # last element
