class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    
        cnt = numBottles
        while numBottles != 0 and numBottles >= numExchange:
            dr = numBottles // numExchange
            lftb = numBottles % numExchange
            cnt += dr
            numBottles = dr + lftb
        return cnt