class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        win = deque()
        n = len(p)
        res = []
        l, r = 0, 0
        h = n-1
        k = sorted(p)
        while r < len(s):
            win.append(s[r])
            if r - l + 1 == n:
                if sorted(win) == k:
                    res.append(r-h)
                win.popleft()
                r += 1
                l += 1
            else:
                r += 1

        return res
