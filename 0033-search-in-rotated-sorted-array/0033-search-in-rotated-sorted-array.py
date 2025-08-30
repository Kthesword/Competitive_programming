class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = -1
        l, r = 0, n - 1
        def findPivot(l, r):
            while l < r:
                mid = (r+l) // 2

                leftNum = nums[l]
                leftToMid = nums[mid-1]
                middle = nums[mid]
                rightToMid = nums[mid+1]

                if middle > rightToMid:
                    return mid + 1
                elif leftToMid > middle:
                    return mid

                if leftNum < middle:
                    l = mid + 1
                else:
                    r = mid - 1

        def binarySearch(l, r):
            while l <= r:
                mid = (l+r) // 2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if nums[0] > nums[-1]:

            pivot = findPivot(l, r)
            if target == nums[pivot]:
                res = pivot
            elif nums[pivot] <= target <= nums[-1]:
                res = binarySearch(pivot, r)
            elif nums[0] <= target >= nums[pivot]:
                res = binarySearch(0, pivot)
        else:
            res = binarySearch(l, r)

        return res
        