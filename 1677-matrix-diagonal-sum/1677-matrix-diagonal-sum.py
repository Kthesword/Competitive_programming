class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        
        res = 0
        # main diagonal
        r, c = 0, 0
        while r < n and c < n:
            res += mat[r][c]
            r += 1
            c += 1
        
        # secendary diagonal
        r, c = 0, n-1
        while r < n and 0 <= c < n:
            res += mat[r][c]
            r += 1
            c -= 1
        
        if n % 2:
            return res - mat[n//2][n//2]
        return res