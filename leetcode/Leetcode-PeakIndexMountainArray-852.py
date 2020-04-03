class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if A is None or len(A) < 3:
            return -1

        start, end = 0, len(A) - 1

        while start < end:
            mid = (start + end) // 2
            if not 0 <= A[mid] <= 10 ** 6:
                return -1
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


A = [0, 1, 0]
s = Solution()
print(s.peakIndexInMountainArray(A))
A = [0, 2, 1, 0]
print(s.peakIndexInMountainArray(A))
