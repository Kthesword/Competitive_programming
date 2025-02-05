class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        d = int("".join(s)) + 1
        c = str(d)
        n = list(map(int, c))
        return n