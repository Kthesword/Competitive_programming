class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0 
        d = set()
        for r in range(len(s)):
            c = s[r]
            if c in d:
                while c in d:
                    d.discard(s[l])
                    l += 1
            d.add(c)
            res = max(res, len(d))
        return res

