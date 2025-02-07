class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tofnd = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in tofnd:
                return [i, tofnd[k]]
            tofnd[nums[i]] = i
