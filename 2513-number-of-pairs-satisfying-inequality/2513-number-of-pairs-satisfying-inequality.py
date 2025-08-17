class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        res = 0
        so_li = SortedList()
        
        for i in range(n):
		
#           If rhs is in the list (applying binary search)
            res += so_li.bisect_right(nums1[i]-nums2[i]+diff)
			
#           adding lhs in the left side 
            so_li.add(nums1[i] - nums2[i])
			
        return res