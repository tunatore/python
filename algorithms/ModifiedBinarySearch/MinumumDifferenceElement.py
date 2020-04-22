
def search_min_diff_element(arr, key):
    start = 0
    end = len(arr)
    last_index = 0

    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
            last_index = end - 1
        elif key > arr[mid]:
            start = mid + 1
            last_index = start - 1
        elif key == arr[mid]:
            return arr[mid]

    return arr[last_index]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
