class Solution:
    def addDigits(self, num: int) -> int:
        def add(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
            
        while num // 10 > 0:
            num = add(num)

        return num