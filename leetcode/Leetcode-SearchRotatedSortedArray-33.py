class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums)
        left_bound_visited = False
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                if target > nums[0] and nums[len(nums) - 1] < target and left_bound_visited is False:
                    left_bound_visited = True
                    start = 0
                    end = mid - 1
                elif target < nums[0] and nums[len(nums) - 1] > target and left_bound_visited is False:
                    left_bound_visited = True
                    start = mid + 1
                    end = len(nums)
                else:
                    end = mid
            elif target > nums[mid]:
                if nums[len(nums) - 1] < target and nums[0] < target:
                    start = mid + 1
                else:
                    start = 0
                    end = mid - 1
            elif target == nums[mid]:
                return mid
        return -1


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
# print(s.search(nums, 0))
# print(s.search(nums, 1))
# print(s.search(nums, 2))
# print(s.search(nums, 4))
# print(s.search(nums, 5))
# print(s.search(nums, 6))
# print(s.search(nums, 7))
# print(s.search(nums, 8))
# print(s.search(nums, 16))
nums = [8, 0, 1, 2, 3, 4, 5, 6]
print(s.search(nums, 0))
print(s.search(nums, 1))
