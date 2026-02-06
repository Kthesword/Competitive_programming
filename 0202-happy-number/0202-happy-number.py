class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitSquareSum(num):
            s = 0
            while num > 0:
                s += (num % 10) ** 2
                num //= 10
            return s
        d = {2, 4, 16, 37, 58, 89, 145, 42, 20}
        if n == 1:
            return True
        if n in d:
            return False
        while True:
            if n == 1:
                return True
            if n in d:
                return False
            print(n)
            n = getDigitSquareSum(n)
        