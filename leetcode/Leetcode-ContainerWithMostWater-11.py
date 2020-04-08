class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left = 0
        right = len(height) - 1
        while left <= right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 1]))
print(s.maxArea([1, 8, 7, 6, 5, 9]))
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
