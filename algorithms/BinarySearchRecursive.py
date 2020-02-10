import math


def recursive_binary_search(arr, start, end, key):
    if start < end:
        mid = math.floor((start + end) / 2)
        if key < arr[mid]:
            return recursive_binary_search(arr, start, mid, key)
        elif key > arr[mid]:
            return recursive_binary_search(arr, mid + 1, end, key)
        elif key == arr[mid]:
            return mid

    return -1


array = [10, 40, 50, 90, 80, 70, 20, 30, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18]
print("Sorted array: ", sorted(array))
key = 11

found = recursive_binary_search(sorted(array), 0, len(array), key)
if found != -1:
    print("found")
else:
    print("Not found")
