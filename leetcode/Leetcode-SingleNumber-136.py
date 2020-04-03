class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = dict([])

        for i in nums:
            if i not in d:
                d[i] = i
            else:
                del d[i]
        return list(d.values())[0]

                