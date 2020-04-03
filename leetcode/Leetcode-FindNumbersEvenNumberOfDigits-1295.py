class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not 1 <= len(nums) <= 500:
            return None

        count = 0
        for i in nums:
            if not 1 <= i <= 10 ** 5:
                return None
            if len(str(i)) % 2 == 0:
                count += 1
        return count
        