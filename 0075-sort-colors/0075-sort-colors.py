class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        # left, right = 0, len(nums) - 1
        # i = 0
        # while i <= right:
        #     if nums[i] == 0:
        #         left, i = i, left
        #         left += 1
        #     elif nums[i] == 2:
        #         i, right = right, i
        #         right -= 1
        #         i -= 1
        #     i += 1
            