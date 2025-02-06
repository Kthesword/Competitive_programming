class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        rl = []
        ln = len(nums)
        for i in range(ln):
            x = nums[i]
            if nums[i] == 0:
                rl.append(x)
            elif nums[i] > 0:
                rl.append(nums[(i+x)%ln])
            else:
                rl.append(nums[(i-abs(x))%ln])
        return rl
