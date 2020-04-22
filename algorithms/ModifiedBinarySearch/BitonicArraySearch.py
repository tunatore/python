# modified binary search


# Time complexity - O(logN) and Space complexity O(1)
def search_bitonic_array(arr, key):

    max_index = find_max_index_in_bitonic_array(arr)

    # search ascending part
    start, end = 0, max_index + 1
    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
        elif key > arr[mid]:
            start = mid + 1
        elif key == arr[mid]:
            return mid

    # search descending part
    start, end = max_index, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
        elif key > arr[mid]:
            start = mid - 1
        elif key == arr[mid]:
            return mid
    return -1


def search_bitonic_array1(arr, key):
    maxIndex = find_max(arr)
    keyIndex = binary_search(arr, key, 0, maxIndex)
    if keyIndex != -1:
        return keyIndex
    return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # at the end of the while loop, 'start == end'
    return start


def find_max_index_in_bitonic_array(arr):

    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid+1]:  # each time divide 2 and mid + 1 doesn't cause overflow
            end = mid
        else:
            start = mid + 1
    return start


# order-agnostic binary search
def binary_search(arr, key, start, end):
    while start <= end:
        mid = int(start + (end - start) / 2)

        if key == arr[mid]:
            return mid

        if arr[start] < arr[end]:  # ascending order
            if key < arr[mid]:
                end = mid - 1
            else:  # key > arr[mid]
                start = mid + 1
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1
            else:  # key < arr[mid]
                start = mid + 1

    return -1  # element is not found


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
