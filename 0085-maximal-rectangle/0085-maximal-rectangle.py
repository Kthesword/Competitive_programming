from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        rows = len(matrix)
        cols = len(matrix[0])
        histo = [0] * cols
        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j])
                if matrix[i][j] == "1":
                    histo[j] += 1
                else:
                    histo[j] = 0
                
                stack = []
            for i in range(cols + 1):
                cur_height = histo[i] if i < cols else 0
                while stack and histo[stack[-1]] > cur_height:
                    h = histo[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
