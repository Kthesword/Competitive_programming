class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        bags = []
        for i in range(n - 1):
            bags.append(weights[i] + weights[i + 1])

        bags.sort()
        i = k - 1

        max_score = sum(bags[-i:])
        min_score = sum(bags[:i])

        return max_score - min_score