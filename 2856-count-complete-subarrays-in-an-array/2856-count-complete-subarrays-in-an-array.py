class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        n = len(nums)
        res = 0

        for left in range(n):
            seen = set()
            for right in range(left, n):
                seen.add(nums[right])
                if len(seen) == total_unique:
                    res += 1  
        return res
