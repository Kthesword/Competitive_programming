class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key = lambda t : t[0])
        n = len(tasks)
        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < n:
            while i < n and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if minHeap:
                ptime, index = heappop(minHeap)
                res.append(index)
                time += ptime
            else:
                time = tasks[i][0]

        return res


