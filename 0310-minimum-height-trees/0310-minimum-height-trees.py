class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Create an adjacency list representation of the tree
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        # Initialize leaves set with nodes having degree 1
        leaves = deque([i for i in range(n) if len(adj_list[i]) == 1])

        # Repeatedly remove leaves until 1 or 2 nodes left
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()  # Remove leaf
                adj_list[neighbor].remove(leaf)  # Remove back reference
                if len(adj_list[neighbor]) == 1:  # New leaf found
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)