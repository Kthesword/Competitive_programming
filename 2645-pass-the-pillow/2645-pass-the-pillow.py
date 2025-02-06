class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n-= 1
        time%= n+n
        p = n+1 - abs(n - time)
        return p