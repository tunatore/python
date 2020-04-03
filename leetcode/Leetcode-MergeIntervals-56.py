class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if intervals is None:
            return None

        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda interval: interval[0]) # sort with start
        merged = []
        start, end = intervals[0][0], intervals[0][1]

        for index in range(1, len(intervals)):
            interval = intervals[index]
            if interval[0] <= end:  # overlap
                end = max(interval[1], end)
            else:  # not overlapping
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
        # last interval
        merged.append([start, end])
        return merged


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [4, 5]]))
print(s.merge([[1, 4], [1, 4]]))
print(s.merge([[1, 4], [4, 5], [1, 10]]))
print(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
