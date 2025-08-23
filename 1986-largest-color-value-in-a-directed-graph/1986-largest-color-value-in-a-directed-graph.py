class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges: 
            graph[src].append(dst)
        
        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0

            path.add(node)
            visit.add(node)

            colorIndex = ord(colors[node]) - ord("a")
            count[node][colorIndex] = 1

            for nei in graph[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")

                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        count[nei][c] + ( 1 if c == colorIndex else 0)
                    )
                
            path.remove(node)
            return max(count[node])

        n, res = len(colors), 0
        count = [[0] * 26 for i in range(n)]
        path, visit = set(), set()

        for i in range(n):
            res = max(res, dfs(i))
        
        return -1 if res == float("inf") else res