class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n + m - 1
        while min(n, m) > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1

            i -= 1
        
        while n > 0:
            nums1[i] = nums2[n-1]
            n -= 1
            i -= 1


