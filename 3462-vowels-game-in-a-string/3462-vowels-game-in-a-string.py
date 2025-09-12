class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vows = sum([1 for c in s if c in {"a", "e", "i", "o", "u"}])
        if vows:
            return True
        
        return False