class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.min = 1

    
    def popSmallest(self) -> int:
        if self.heap:
            return heappop(self.heap)
            
        self.min += 1
        return self.min - 1
                

    def addBack(self, num: int) -> None:
        if num < self.min and num not in self.heap:
            heappush(self.heap, num)
        

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)