class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        islands = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                if inbound(newr, newc) and not visited[newr][newc] and grid[newr][newc] == "1":
                    dfs(newr, newc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    dfs(row, col)

        return islands
