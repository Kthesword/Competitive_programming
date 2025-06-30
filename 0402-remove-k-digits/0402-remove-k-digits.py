class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for dig in num:
            while k and stack and stack[-1]>dig:
                stack.pop()
                k -= 1
            if not stack and dig == '0':
                continue
            stack.append(dig)
        return "0" if not stack or k>=len(stack) else "".join(stack[:len(stack)-k])