class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  # (max elevation so far, x, y)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
        
        while heap:
            time, x, y = heapq.heappop(heap)
            # If we reach the bottom-right, return the time (max elevation so far)
            if x == n - 1 and y == n - 1:
                return time
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    # Push the max elevation encountered so far
                    heapq.heappush(heap, (max(time, grid[nx][ny]), nx, ny))