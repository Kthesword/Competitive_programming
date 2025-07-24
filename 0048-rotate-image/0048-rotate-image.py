class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, right = 0, n-1    
        while left < right:
            for i in range(right-left):
                top, bottom = left, right    
                topleft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom - i][left]
                matrix[bottom-i][left] = matrix[bottom][right - i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topleft
            left += 1
            right -= 1