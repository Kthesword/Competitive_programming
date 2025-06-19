class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            
            bricks -= diff
            heappush(heap, -diff)
            
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heappop(heap)
        
        return n-1
        