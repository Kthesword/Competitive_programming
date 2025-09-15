class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bl = set(brokenLetters)
        res = 0
        for word in text.split():
            wd = set(word)
            h = False
            for c in wd:
                if c in bl:
                    h = True
                    break
            if not h:
                res += 1
        
        return res