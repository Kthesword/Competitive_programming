class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            s = str(nums[i])
            s = s[::-1]
            nums.append(int(s))
        ans = set(nums)
        return len(ans)