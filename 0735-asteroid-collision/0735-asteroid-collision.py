class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for curr in asteroids:
            while stack and curr < 0 < stack[-1]:
                if stack[-1] < -curr:
                    stack.pop()
                    continue
                elif stack[-1] == -curr:
                    stack.pop()
                    break
                break
            else:
                stack.append(curr)
        return stack