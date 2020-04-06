class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0:
            return None

        result = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        size = len(matrix) * len(matrix[0])
        while len(result) < size:
            for i in range(left, right + 1):
                if len(result) < size:
                    result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                if len(result) < size:
                    result.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                if len(result) < size:
                    result.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                if len(result) < size:
                    result.append(matrix[i][left])
            left += 1
        return result


s = Solution()
print(s.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(s.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
