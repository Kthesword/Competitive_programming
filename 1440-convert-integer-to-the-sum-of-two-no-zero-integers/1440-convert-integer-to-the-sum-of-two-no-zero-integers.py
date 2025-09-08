class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        for i in range(n-1,0,-1):
            if not "0" in str(a) and not "0" in str(i):
                if i + a == n:
                    return [a, i]
            
            a += 1