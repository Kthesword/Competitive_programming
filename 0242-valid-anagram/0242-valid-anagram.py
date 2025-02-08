
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds, dt = Counter(s), Counter(t)
        st = set(s)
        ans = True
        for ch in st:
            ans = ds[ch] == dt[ch]
            if ans == False:
                return ans
        return ans