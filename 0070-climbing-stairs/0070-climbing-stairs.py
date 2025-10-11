class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2:
                return i
            if not i in memo:
                memo[i] = dp(i-1) + dp(i-2)
            
            return memo[i]
        
        memo = {}
        return dp(n)