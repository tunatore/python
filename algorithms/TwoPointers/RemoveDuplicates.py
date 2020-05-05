# Two pointers


# Time complexity: O(N) and Space complexity O(1)
def remove_duplicates(arr):

    if arr is None:
        return 0

    if len(arr) < 2:
        return 1

    count, left, right = 1, 0, 1
    while right <= len(arr) - 1:
        if arr[left] == arr[right]:
            right += 1
        elif arr[left] != arr[right]:
            count += 1
            left = right
            right += 1
    return count


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
print(remove_duplicates([2, 2, 2, 11]))  # 2
