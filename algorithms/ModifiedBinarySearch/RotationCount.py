# Modified Binary search


# Time complexity 0(logN) and Space complexity O(1)
def count_rotations(arr):
    start, end = 0, len(arr) - 1
    if arr[start] < arr[end]:
        return 0

    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid-1]:  # each time divide 2 and mid + 1 doesn't cause overflow
            return arr[mid-1]
        elif arr[0] > arr[mid]:
            end = mid
        else:
            start = mid + 1
    return arr[start-1]


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([4, 5, 7, 9, 10, 11, 12, -1, 2]))
    print(count_rotations([12, -1, 2]))
    print(count_rotations([11, 12, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    print(count_rotations([15, 1, 3, 8, 10]))
    print(count_rotations([15, 18, 1, 3, 8, 10, 11, 12, 13]))


main()
