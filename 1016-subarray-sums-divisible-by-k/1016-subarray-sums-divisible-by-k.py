class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        mod_count = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod < 0:
                mod += k
            
            if mod in mod_count:
                count += mod_count[mod]
        
            if mod in mod_count:
                mod_count[mod] += 1
            else:
                mod_count[mod] = 1
        
        return count