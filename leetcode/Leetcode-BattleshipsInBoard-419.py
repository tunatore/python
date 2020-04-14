class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        number_of_ships = 0
        for row_index in range(len(board)):
            for column_index in range(len(board[row_index])):
                if board[row_index][column_index] == 'X':
                    number_of_ships += 1
                    self.dfs_count_battleship(row_index, column_index, board)

        return number_of_ships

    def dfs_count_battleship(self, row, column, grid):
        if (row < 0 or row >= len(grid)) or (column < 0 or column >= len(grid[0])) or (grid[row][column] == "."):
            return

        grid[row][column] = "."
        self.dfs_count_battleship(row - 1, column, grid)  # up
        self.dfs_count_battleship(row + 1, column, grid)  # down
        self.dfs_count_battleship(row, column - 1, grid)  # left
        self.dfs_count_battleship(row, column + 1, grid)  # right


s = Solution()
print(s.countBattleships([["X", ".", ".", "X"],
                          [".", ".", ".", "X"],
                          [".", ".", ".", "X"]]))
