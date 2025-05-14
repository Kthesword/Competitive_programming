class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones = bin(num2).count("1")

        x = 0
        for i in range(32, -1, -1):
            if ones == 0:
                break
                
            if num1 & (1 << i):  
                x |= 1 << i 
                ones -= 1

        for i in range(32):
            if ones == 0:
                break

            if not (num1 & (1 << i)): 
                x |= 1 << i  
                ones -= 1

        return x