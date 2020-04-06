class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                if grid[row_index][column_index] == 1:
                    max_area = max(max_area, self.dfs(row_index, column_index, grid))
        return max_area

    def dfs(self, row, column, grid):
        if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid[0])) or (grid[row][column] == 0):
            return 0
        grid[row][column] = 0
        count = 1
        count += self.dfs(row - 1, column, grid)  # up
        count += self.dfs(row + 1, column, grid)  # down
        count += self.dfs(row, column - 1, grid)  # left
        count += self.dfs(row, column + 1, grid)  # right
        return count


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
s = Solution()
print(s.maxAreaOfIsland(grid))
