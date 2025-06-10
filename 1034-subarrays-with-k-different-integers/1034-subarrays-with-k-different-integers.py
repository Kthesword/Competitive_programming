class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k): 
            n = len(nums) 
            l, r = 0, 0  
            winmap = {}  
            ans = 0  

            while r < n: 
                if nums[r] not in winmap:  
                    winmap[nums[r]] = 1  
                else:
                    winmap[nums[r]] += 1 

                while len(winmap) > k:  
                    winmap[nums[l]] -= 1  
                    if winmap[nums[l]] == 0:  
                        del winmap[nums[l]]  
                    l += 1 

                ans += (r - l + 1)
                r += 1  

            return ans
        
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k-1)