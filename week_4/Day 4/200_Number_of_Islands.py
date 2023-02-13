from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        island = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    self.helper(row, col, ROW, COL, grid)
                    island += 1

        return island

    def helper(self, row, col, ROW, COL, grid):
        if row in range(ROW) and col in range(COL) and grid[row][col] == "1":
            grid[row][col] = "#"

            direction = [(row, col - 1), (row, col + 1), (row + 1, col), (row - 1, col)]

            for r, c in direction:
                self.helper(r, c, ROW, COL, grid)