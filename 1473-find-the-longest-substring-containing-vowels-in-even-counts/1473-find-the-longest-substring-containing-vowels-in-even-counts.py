class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):

                l = s[j:j+i]
                odd = 0

                for vow in "aeiou":
                    if l.count(vow) % 2 != 0:
                        odd = True
                        break

                if not odd:
                    return i

        return 0