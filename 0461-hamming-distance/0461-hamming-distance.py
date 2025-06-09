class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        xor = x ^ y
        while xor:
            dist += (xor & 1)
            xor >>= 1
        return dist