class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []
        for ch in s:
            if ch == "#":
                if sstack:
                    sstack.pop()
            else:
                sstack.append(ch)
        for ch in t:
            if ch == "#":
                if tstack:
                    tstack.pop()     
            else:
                tstack.append(ch) 
        return sstack == tstack