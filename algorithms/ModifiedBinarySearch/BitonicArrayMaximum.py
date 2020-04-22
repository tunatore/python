# modified binary search


# Time complexity O(N) - Space complexity O(1)
def find_max_in_bitonic_array(arr):

    start, end = 0, len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid+1]:  # each time divide 2 and mid + 1 doesn't cause overflow
            end = mid
        else:
            start = mid + 1
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
