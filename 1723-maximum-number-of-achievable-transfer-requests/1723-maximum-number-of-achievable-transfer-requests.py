class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        rq = len(requests)
        for k in range(rq, 0, -1):

            for comb in combinations(range(rq), k):
                degree = [0] * n

                for i in comb:
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1

                if not any(degree):
                    return k

        return 0