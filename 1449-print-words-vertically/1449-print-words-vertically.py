class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        i = 0
        words = s.split()
        n = max([len(word) for word in words])
        while i <= n:
            cur = []
            for s in words:
                if i > len(s) - 1:
                    cur += " "
                else:
                    cur += [s[i]]
            if cur:
                w = "".join(cur).rstrip()
                if w:
                    res.append(w)
            i += 1
        return res
