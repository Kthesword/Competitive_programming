class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k * "B" in blocks:
            return 0
        
        n = len(blocks)
        l = 0
        wb = defaultdict(int)
        for i in range(k):
            wb[blocks[i]] += 1
        res = wb["W"]
        for r in range(k,n):
            wb[blocks[r]] += 1
            wb[blocks[l]] -= 1
            res = min(res, wb["W"])
            l += 1
        return res

