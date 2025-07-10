class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        # find index using binary search
        n = len(nums)
        if target > nums[n-1]:
            return n
        l, r = 0, n - 1
        mid = (l+r) // 2
        while l <= r:
            mid = (l+r) // 2
            print(nums[mid])
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return l
       