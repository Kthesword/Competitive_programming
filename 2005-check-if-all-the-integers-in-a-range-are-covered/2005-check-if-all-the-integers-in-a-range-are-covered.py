class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            f = False
            for r in ranges:
                if r[0] <= num <= r[1]:
                    f = True
                    break
            
            if not f:
                return False
        
        return True