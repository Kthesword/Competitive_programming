class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)            
        n = len(nums)
        left = 0
        count = 0
        window = Counter()                 
        for right in range(n):
            window[nums[right]] += 1
            
            while window[mx] >= k:
                count += (n - right)
                
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        
        return count