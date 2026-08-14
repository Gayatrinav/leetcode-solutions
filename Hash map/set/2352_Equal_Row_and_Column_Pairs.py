class Solution:
    def equalPairs(self, grid):
        row_count = {}

        # Store frequency of each row
        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1

        ans = 0
        n = len(grid)

        # Check each column
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))

            if col in row_count:
                ans += row_count[col]

        return ans