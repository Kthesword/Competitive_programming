class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        i, j = 0, 0
        arr = []
        while len(arr) < rows*cols:
            while i >= 0 and j < cols:
                arr.append(mat[i][j])
               
                i -= 1
                j += 1
            i += 1
            j -= 1

            if i == rows-1 and j == cols-1:
                break
            
            if j + 1 < cols:
                j += 1
            else:
                i += 1
                  
            while i < rows and j >= 0:
                curr = mat[i][j]
                arr.append(curr)
                i += 1
                j -= 1
            i -= 1
            j += 1

            if i == rows-1 and j == cols-1:
                break

            if i + 1 < rows:
                i += 1
            else:
                j += 1

        return arr
                