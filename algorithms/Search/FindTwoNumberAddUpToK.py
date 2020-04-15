def binary_search(list, search_key):

    start = 0
    end = len(list)

    while start < end:
        mid = (start + end) // 2
        if search_key < list[mid]:
            end = mid
        elif search_key > list[mid]:
            start = mid + 1
        elif search_key == list[mid]:
            return mid
    return -1

# binary search implementation
# Time complexity O(nlogn) and Space complexity O(1)


def findNumbersAddUpToK(list, k):

    if list is None or len(list) == 0:
        return -1

    list.sort()

    for i in range(len(list)):
        index = binary_search(list, k - list[i])
        if index != -1 and index != i:
            return list[i], k - list[i]
    return -1


print(findNumbersAddUpToK([], 1256))
print(findNumbersAddUpToK([1, 2, 3, 4, 5], 7))
print(findNumbersAddUpToK([1, 3, 4, 5], 2))
print(findNumbersAddUpToK([1, 2, 3, 4, 5], 5))

