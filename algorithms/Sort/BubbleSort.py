intList = [10, 40, 50, 90, 80, 70, 20, 30, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18]
print("Unsorted: ", intList)


# bubble sort algorithm implementation
def swap(j, j1):
    intList[j], intList[j1] = intList[j1], intList[j]
    return list


for i in range(len(intList)):
    for j in range(len(intList) - i - 1):
        if intList[j] > intList[j + 1]:
            swap(j, j + 1)

print("Sorted: ", intList)
