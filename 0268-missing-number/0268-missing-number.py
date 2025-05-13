class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        arr_xor = 0
        range_xor = 0
        for i in range(n+1):
            range_xor ^= i
        for i in nums:
            arr_xor ^= i

        return range_xor ^ arr_xor
