class Solution:
    def longestPrefix(self, s: str) -> str:
        k = ""
        for i in range(1, len(s)):
            if s[0:i] == s[len(s)-i:]:
                k = s[0:i]
        return k