class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i = 0
        ans = []
        dirc = 'up'
        x,y = 0, 0
        while i < m + n - 1:
            if 0 <= x < m and 0 <= y < n:
                ans.append(mat[x][y])
    
            if dirc == 'up':
                if y+1 < n and x-1 >= 0:
                    x -= 1
                    y += 1
                else:
                    dirc = 'down'
                    y += 1
                    i += 1
            else:
                if x+1 < m and y-1 >= 0:
                    x += 1
                    y -= 1
                else:
                    dirc = 'up'
                    x += 1
                    i += 1

        return ans
                