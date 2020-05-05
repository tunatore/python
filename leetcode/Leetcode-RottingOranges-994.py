class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return None

        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                if grid[row_index][column_index] == 2:
                    self.rot_oranges(grid, row_index, column_index, 2)

        max_minute = 2
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                if grid[row_index][column_index] == 1:
                    return -1
                max_minute = max(max_minute, grid[row_index][column_index])
        return max_minute - 2

    def rot_oranges(self, grid, i, j, minutes):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or \
                grid[i][j] == 0 or 1 < grid[i][j] < minutes:
            return
        else:
            grid[i][j] = minutes
            self.rot_oranges(grid, i + 1, j, minutes + 1)
            self.rot_oranges(grid, i - 1, j, minutes + 1)
            self.rot_oranges(grid, i, j + 1, minutes + 1)
            self.rot_oranges(grid, i, j - 1, minutes + 1)


s = Solution()
print(s.orangesRotting([[2, 1, 1],
                        [1, 1, 0],
                        [0, 1, 1]]))
print(s.orangesRotting([[2, 1, 1],
                        [0, 1, 1],
                        [1, 0, 1]]))
print(s.orangesRotting([[1, 2]]))