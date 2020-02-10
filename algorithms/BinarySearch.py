import math


def iterative_binary_search(arr, start, end, searchKey):

    while start < end:
        mid = math.floor((start + end) / 2)
        if searchKey < arr[mid]:
            end = mid
        elif searchKey > arr[mid]:
            start = mid + 1
        elif searchKey == arr[mid]:
            return mid

    return -1


array = [10, 40, 50, 90, 80, 70, 20, 30, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18]
print("Sorted array: ", sorted(array))
key = 90
found = iterative_binary_search(sorted(array), 0, len(array), key)
if found != -1:
    print("found")
else:
    print("Not found")
