class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if not n % 2: # even 
            for i in range(1, n // 2 +1):
                ans.extend([i, -i])
        else:
            ans = [0]
            for i in range(1, n//2 +1):
                ans.extend([i, -i])

        return ans


            

