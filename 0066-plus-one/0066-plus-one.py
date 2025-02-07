class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(d) for d in digits])) 
        num2 = num+1
        lnum2 = list(map(int, str(num2)))
        return lnum2