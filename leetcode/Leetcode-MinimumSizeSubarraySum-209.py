class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        window_sum = 0
        window_start_index, window_end_index = 0, 0
        min_length = float('inf')
        min_length_sum = 0

        for window_end_index in range(len(nums)):
            window_sum += nums[window_end_index]
            min_length_sum += 1
            while window_sum >= s:
                if min_length_sum < min_length:
                    min_length = min_length_sum
                window_sum -= nums[window_start_index]
                min_length_sum -= 1
                window_start_index += 1

        if min_length == float('inf'):
            return 0

        return min_length


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
