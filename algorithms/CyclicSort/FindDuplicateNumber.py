# cyclic sort


# Time complexity O(N) and Space complexity O(1)
def find_duplicate(nums):
    if nums is None:
        return nums

    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        if nums[start_index] != start_index + 1:
            index = nums[start_index]
            if nums[start_index] != nums[index - 1]:
                #  swap
                temp = nums[index - 1]
                nums[index - 1] = nums[start_index]
                nums[start_index] = temp
                # nums[start_index], nums[index -1] = nums[index -1], nums[start_index]
            else:
                return nums[start_index]
        else:
            start_index += 1
    return -1


nums = [1, 4, 4, 3, 2]
print(find_duplicate(nums))

nums = [2, 1, 3, 3, 5, 4]
print(find_duplicate(nums))

nums = [2, 4, 1, 4, 4]
print(find_duplicate(nums))

nums = [2, 3, 1, 1, 4, 5]
print(find_duplicate(nums))