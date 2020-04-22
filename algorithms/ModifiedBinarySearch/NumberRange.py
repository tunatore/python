# modified binary search


# Time complexity O(logN) and Space complexity O(1)
def find_range(arr, key):
    result = [- 1, -1]

    result[0] = binary_search(arr, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)

    if result[0] != -1 and result[0] != -1:
        return [result[0], result[1]]
    else:
        return result


def binary_search(arr, key, find_max):

    start = 0
    end = len(arr)
    index = -1
    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
        elif key > arr[mid]:
            start = mid + 1
        elif key == arr[mid]:
            index = mid
            if find_max is False:
                end = mid
            else:
                start = mid + 1
    return index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
