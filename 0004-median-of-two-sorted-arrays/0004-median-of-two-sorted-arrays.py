class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        n, m = len(nums1), len(nums2)
        p1, p2 = 0, 0
        while p1 < n and p2 < m:
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1
        if p1 < n:
            merged += nums1[p1:]
        if p2 < m:
            merged += nums2[p2:]
    
        if (n+m) % 2 == 0:
            mid = (n+m - 2) // 2
            median = (merged[mid] + merged[mid+1]) / 2
            return median
        else:
            mid = (n+m) // 2
            return merged[mid]