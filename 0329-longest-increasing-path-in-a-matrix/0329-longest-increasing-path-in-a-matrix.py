class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(matrix), len(matrix[0])
        visited = {}
        def dfs(x, y, prev):
            if (x < 0 or x == n or 
                y < 0 or y == m or
                matrix[x][y] <= prev):
                return 0
            
            if (x, y) in visited: 
                return visited[(x, y)]

            res = 1
            for xc, yc in dirs:
                nx, ny = x + xc, y + yc
                res = max(res, 1 + dfs(nx, ny, matrix[x][y]))
                # print(i,j,curmax, "lkj", matrix[x][y])
            visited[(x,y)] = res
            return res
# visited = set()

        lip = 1
        for i in range(n):
            for j in range(m):
                lip = max(lip, dfs(i, j, -1))
        
        return lip
