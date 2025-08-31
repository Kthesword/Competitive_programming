class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sl = SortedList()
        res = 0
        for n in instructions:
            res += min(sl.bisect_left(n), len(sl)-sl.bisect_right(n))
            sl.add(n)
            
        return res%(10**9+7)