class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        bf = prices[0]
        for pr in prices:
            res = max(res, pr - bf)
            bf = min(bf, pr)
        return res
