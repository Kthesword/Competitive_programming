class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        se = set()
        for rang in ranges:
            for i in range(rang[0],rang[1] + 1):    
                se.add(i)
        ans = True
        for i in range(left, right + 1):
            if i not in se:
                ans = False
                break
        return ans