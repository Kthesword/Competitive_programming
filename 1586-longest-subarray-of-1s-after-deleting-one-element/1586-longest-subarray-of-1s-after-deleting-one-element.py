class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, left, prefix = 0, 0, 0

        for right, n in enumerate(nums):
            prefix += n
            while prefix < right - left:
                prefix -= nums[left]
                left += 1
            res = max(res, right - left)

        return res