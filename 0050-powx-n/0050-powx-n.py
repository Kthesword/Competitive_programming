class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1 / pow(x, -n)
            half = pow(x, n//2)
            if not n % 2: # if n is even
                return half * half
            else: # if n is odd
                return half * half * x
        
        return pow(x, n)
            