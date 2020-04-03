class Solution(object):
    def sortedSquares(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        if not 1 <= len(A) <= 10000:
            return None

        for i in range(0, len(A)):
            if not -10000 <= A[i] <= 10000:
                return None
            else:
                A[i] = A[i] * A[i]
        return sorted(A)


s = Solution
A = [-4, -1, 0, 3, 10]
print(s.sortedSquares(A))
