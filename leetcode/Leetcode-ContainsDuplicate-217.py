class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        d = dict([])

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1

        dict_values = {key: value for (key, value) in d.items() if value > 1}
        return len(dict_values.values()) != 0


numbers = [1, 2, 3, 1]
s = Solution()
print(s.containsDuplicate(numbers))
