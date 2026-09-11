class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        get = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in get:
                res.extend([i, get[diff]])
                return res
            else:
                get[nums[i]] = i
            
