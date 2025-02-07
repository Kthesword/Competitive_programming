class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}#defaultdict(int)
        dt = {}#defaultdict(int)
        for ch in s:
            ds[ch] = ds.get(ch,0) + ds.get(ch,1)
        for ch in t:
            dt[ch] = dt.get(ch,0) + dt.get(ch,1)
        return ds == dt
