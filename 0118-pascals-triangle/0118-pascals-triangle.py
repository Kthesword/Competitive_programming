class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        a = [1]
        for j in range(numRows-1):
            p = [1] * (len(a) + 1)
            for i in range(1, len(a)):
                p[i] = a[i-1] + a[i]
            a = p
            res.append(p)
        return res