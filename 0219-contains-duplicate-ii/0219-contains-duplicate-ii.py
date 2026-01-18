class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = {}
        l = 0
        for r in range(n):
            while r - l > k:
                del d[nums[l]]
                l += 1

            if nums[r] in d:
                return True
            d[nums[r]] = r

        return False