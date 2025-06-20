class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        
        while left != right:
            left = left >> 1
            right = right >> 1
            cnt += 1
        
        return left << cnt