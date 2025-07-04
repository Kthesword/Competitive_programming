class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        prev = [0] * n
        res = 0
        for row in matrix:
            curr = [e + 1 if cell == '1' else 0 for e, cell in zip(prev, row)]
            curr.append(0)
            stack = [(0, -1)]
            for i, e in enumerate(curr):
                while e < stack[-1][0]:
                    length, _ = stack.pop()
                    res = max(res, min(length, i - stack[-1][1] - 1) ** 2)
                stack.append((e, i))
            curr.pop()
            prev = curr
        return res