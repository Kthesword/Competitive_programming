class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            subarray = cursum = 0
            for n in nums:
                cursum += n
                if cursum > largest:
                    subarray += 1
                    cursum = n
                
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        