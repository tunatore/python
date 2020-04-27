# cyclic sort


# Time complexity O(N) and Space complexity O(1)
def cyclic_sort(nums):
    if nums is None:
        return nums

    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        index = nums[start_index]
        if nums[start_index] != nums[index - 1]:
            #  swap
            temp = nums[index - 1]
            nums[index - 1] = nums[start_index]
            nums[start_index] = temp
            # nums[start_index], nums[index -1] = nums[index -1], nums[start_index]
        else:
            start_index += 1
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))