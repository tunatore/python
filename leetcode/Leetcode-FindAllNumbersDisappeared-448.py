class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict([])

        for num in nums:
            if num not in d:
                d[num] = 1

        list = []
        for i in range(1, len(nums) + 1):
            if 1 <= nums[i - 1] <= len(nums):
                if d.get(i) is None:
                    list.append(i)
            else:
                return None
        return list


list = [1, 2]
s = Solution()
print(s.findDisappearedNumbers(list))
