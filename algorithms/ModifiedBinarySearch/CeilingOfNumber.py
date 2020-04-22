# modified binary search


# Time complexity O(logN) and Space complexity O(1)
def search_ceiling_of_a_number(arr, key):

    if key > arr[-1]:
        return -1

    start = 0
    end = len(arr)
    max_in_array = 0

    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
        elif key > arr[mid]:
            max_in_array = mid + 1
            start = mid + 1
        elif key == arr[mid]:
            return mid

    return max_in_array


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
