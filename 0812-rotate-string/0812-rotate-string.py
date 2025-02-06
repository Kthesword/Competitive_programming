class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        l = list(s)
        if set(s) == set(goal) and len(s) == len(goal):
            for i in range(len(s)):
                tmp = l[0]
                l.remove(l[0])
                l.append(tmp)
                if goal == "".join(l):
                    return True
        return False
