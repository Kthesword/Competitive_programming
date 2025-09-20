class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        res = [-1, -1] 
        for i in range(n):
            if indexDifference < n:
                for j in range(indexDifference + i, n):
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        return [i, j]

            if i + indexDifference == n:
                break
        
        return res