class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x > 0 or y > 0:
            xb = x & 1
            yb = y & 1
            if xb != yb:
                dist += 1
            x >>= 1
            y >>= 1
        return dist