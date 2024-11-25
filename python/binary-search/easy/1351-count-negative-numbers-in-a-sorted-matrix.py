class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        mRow = len(grid)
        mCol = len(grid[0])

        row = 0
        col = mCol - 1
        count = 0

        while row < len(grid) and col >= 0:
            if grid[row][col] < 0:
                count += mRow - row
                col -= 1
            else:
                row += 1

        return count
