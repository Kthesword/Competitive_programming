class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        qu = collections.deque(arr)

        while len(qu) > k:
            if abs(x - qu[-1]) < abs(x - qu[0]):
                qu.popleft()
            else:
                qu.pop()

        return list(qu)