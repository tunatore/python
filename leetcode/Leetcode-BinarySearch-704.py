class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums is None or len(nums) == 0:
            return None

        if not 1 <= len(nums) <= 10000:
            return None

        return binary_search(nums, 0, len(nums), target)


def binary_search(nums, start, end, target):
    if start < end:
        mid = (start + end) / 2
        if target < nums[mid]:
            return binary_search(nums, start, mid, target)
        elif target > nums[mid]:
            return binary_search(nums, mid + 1, end, target)
        elif target == nums[mid]:
            return mid
    return -1


def check_num(n):
    if -9999 <= n <= 9999:
        return False
    else:
        return True
