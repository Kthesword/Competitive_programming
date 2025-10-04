class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # the ones that appear only 1 time are the head and tail
        adjacencies = defaultdict(set)
        
        # Find head and tail
        for u, v in adjacentPairs:
            adjacencies[u].add(v)
            adjacencies[v].add(u)
            
        head, tail = [key for key, neighbors in adjacencies.items() if len(neighbors) == 1]
        
        res = [head]
        prev = head
        
        while res[-1] != tail:
            _next = adjacencies[prev].pop()   
            adjacencies[_next].remove(prev)
            prev = _next
            
            res.append(_next)
            
        return res