class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isPossible(till):
            prefixSum = [0 for _ in range(len(nums)+1)]
            for i in range(till+1):
                a,b,val = queries[i]
                prefixSum[a] += val
                prefixSum[b+1] -= val
            for i in range(1,len(nums)):
                prefixSum[i] += prefixSum[i-1]
            for i in range(len(nums)):
                if nums[i] > prefixSum[i]: return False
            return True
        
        low = -1 
        high = len(queries)-1
        while low <= high:
            
            mid = (low+high)//2
            print(mid)
            if isPossible(mid):
                if mid==low: return mid+1 
                high = mid
            else:
                low = mid+1
                
        return -1
