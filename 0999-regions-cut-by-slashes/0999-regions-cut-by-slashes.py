class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m,n = len(grid),len(grid[0])
        nr,nc = 3*m,3*n
        grid2 = [[0 for i in range(nc)] for j in range(nr)]

        for r in range(m):
            for c in range(n):
                r2,c2 = r*3,c*3
                if grid[r][c]=='/':
                    grid2[r2][c2+2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2]=1
                elif grid[r][c]=='\\':
                    grid2[r2][c2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2+2]=1
    
        def dfs(r,c):
            if r<0 or r==nr or c<0 or c==nc or grid2[r][c]:
                return 
            
            grid2[r][c]=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        ans = 0
        for i in range(nr):
            for j in range(nc):
                if grid2[i][j] == 0:
                    dfs(i,j)
                    ans += 1

        return ans
