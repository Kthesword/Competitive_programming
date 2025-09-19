class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inDegrees = [0] * n
        for u, v in edges:
            graph[u].append(v)
            inDegrees[v] += 1

        que = deque([i for i in range(n) if inDegrees[i] == 0])
        ans = [set() for i in range(n)]

        while len(que) > 0:
            cur = que.popleft()

            for child in graph[cur]:
                ans[child].add(cur)
                ans[child] |= ans[cur]
                inDegrees[child] -= 1     

                if inDegrees[child] == 0:
                    que.append(child)   
        
        ans = [sorted(list(nodes)) for nodes in ans]
        return ans