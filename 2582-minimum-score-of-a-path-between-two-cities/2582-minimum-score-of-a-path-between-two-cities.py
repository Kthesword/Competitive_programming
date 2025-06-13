class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for start, destin, dist in roads:
            dic[start].append((destin, dist))
            dic[destin].append((start, dist))

        vis = set()
        def dfs(i):
            if i in vis:
                return
            vis.add(i)
            nonlocal res
            for nei, dest in dic[i]:
                res = min(res, dest)
                dfs(nei)

        res = float("inf")
        dfs(1)
        return res
