class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_d = []
        for x, y in points:
            dist = sqrt(x ** 2 + y ** 2)
            heappush(min_d, [dist, [x, y]])
        res = []
        for i in range(k):
            res.append(heappop(min_d)[-1])

        return res 

