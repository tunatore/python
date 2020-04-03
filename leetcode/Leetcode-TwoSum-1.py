class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numbers_seen = {}

        index = -1
        for number in nums:
            index = index + 1
            searched_number = target - number
            if not numbers_seen.get(searched_number) is None:
                return [numbers_seen.get(searched_number), index]
            else:
                numbers_seen[number] = index