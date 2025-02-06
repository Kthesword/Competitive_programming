class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        modcols = []
        for row in range(len(matrix)):
            if 0 in matrix[row]:
                while 0 in matrix[row]:
                    col0 = matrix[row].index(0)
                    matrix[row][col0] = 1
                    modcols.append(col0)
                matrix[row] = [0]*len(matrix[row])
        for idx in modcols:
            for row in matrix:
                row[idx] = 0


            
        