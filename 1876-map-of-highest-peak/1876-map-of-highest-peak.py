class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        result = [[-1] * m for _ in range(n)]
        queue = deque()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(n):
            for j in range(m):
                if(isWater[i][j]==1):
                    result[i][j]=0
                    queue.append((i,j))

        while(queue):
            i,j = queue.popleft()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if(nx >= 0 and nx < n and ny >= 0 and ny < m and result[nx][ny] == -1):
                    result[nx][ny] = result[i][j] + 1
                    queue.append((nx, ny))

        return result