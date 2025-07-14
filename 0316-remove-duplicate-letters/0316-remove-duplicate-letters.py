class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash = {key:i for i, key in enumerate(s) }
        res = []
        seen = set()

        for i, c in enumerate(s):
            if c not in seen:
                while res and c < res[-1] and i < hash[res[-1]]:
                    seen.discard(res[-1])
                    res.pop()
                
                res.append(c)
                seen.add(c)

        
        return "".join(res)



