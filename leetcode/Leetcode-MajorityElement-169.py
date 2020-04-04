class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_times = len(nums) / 2
        d = dict([])
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        for key in d:
            if d[key] > majority_times:
                majority_element = key

        return majority_element


s = Solution()
print(s.majorityElement([3,2,3]))
