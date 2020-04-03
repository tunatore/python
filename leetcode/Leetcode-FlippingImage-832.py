class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(len(A)):
            j = 0
            k = len(A[i]) - 1
            while j < k:
                temp = A[i][j]
                A[i][j] = A[i][k]
                A[i][k] = temp
                j += 1
                k -= 1

            j = 0
            while j < len(A[i]):
                A[i][j] = 0 if A[i][j] == 1 else 1
                j += 1
        return A


s = Solution()
print(s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
