class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort(reverse = True)
        n = len(piles) // 3
        idx = 1
        max_sum =0
        for _ in range(n):
            max_sum += piles[idx]
            idx += 2
        return max_sum 