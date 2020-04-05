class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sum formula
        # s = n (a1 + a2) / 2

        n = len(nums) + 1
        sum_nums = n * (0 + n - 1) / 2
        return sum_nums - sum(nums)




