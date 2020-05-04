# Two pointers


# Time complexity: O(N) and Space complexity O(1)
def pair_with_targetsum(arr, target_sum):

    left_pointer, right_pointer = 0, len(arr) - 1
    while left_pointer < right_pointer:
        if arr[left_pointer] + arr[right_pointer] == target_sum:
            return [left_pointer, right_pointer]
        elif arr[left_pointer] + arr[right_pointer] > target_sum:
            right_pointer -= 1
        elif arr[left_pointer] + arr[right_pointer] < target_sum:
            left_pointer += 1
    return [-1, -1]


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))  # [1,3]
print(pair_with_targetsum([2, 5, 9, 11], 11))  # [0,2]

