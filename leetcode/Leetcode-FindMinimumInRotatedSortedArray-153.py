class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return None

        if len(nums) == 1:
            return nums[0]

        min = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
            else:
                if i + 1 == len(nums) - 1:
                    return min


nums = [3, 4, 5, 1, 2]
s = Solution()
print(s.findMin(nums))