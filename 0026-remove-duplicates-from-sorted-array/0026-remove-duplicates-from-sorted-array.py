class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        vis = set()
        _s = 0
        for num in nums:
            if not num in vis:
                nums[_s] = num
                vis.add(num)
                _s += 1
        
        return _s