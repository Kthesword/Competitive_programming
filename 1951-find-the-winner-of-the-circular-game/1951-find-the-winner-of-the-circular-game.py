class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [i for i in range(1, n + 1)]
        tr = k-1
        nx = l[0]
        np = 0
        i=0
        # 2, 4, 1, 5
        while len(l) != 1:
            np = l.index(nx) + tr
            nx = l[(np + 1) % len(l)]
            l.remove(l[np%len(l)])
            i += 1
        return l[0]