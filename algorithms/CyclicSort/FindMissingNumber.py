# cyclic sort


# Time complexity O(N) and Space complexity O(1)
def find_missing_number(nums):
    if nums is None:
        return nums

    start_index = 0
    end_index = len(nums)

    while start_index < end_index:
        index = nums[start_index]
        if nums[start_index] < len(nums) and nums[start_index] != nums[index]:
            #  swap
            temp = nums[index]
            nums[index] = nums[start_index]
            nums[start_index] = temp
            # nums[start_index], nums[index -1] = nums[index -1], nums[start_index]
        else:
            start_index += 1

    for i in range(len(nums)):
        if i != nums[i]:
            return i


nums = [4, 0, 3, 1]
print(find_missing_number(nums))

nums = [8, 3, 5, 2, 4, 6, 0, 1]
print(find_missing_number(nums))