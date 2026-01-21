class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        _sum = sum(nums)
        operation = 0
        cur_sum = 0
        while cur_sum < _sum:
            cur_sum += k
        
        if cur_sum > _sum:
            operation = _sum + k - cur_sum
        else:
            operation = 0

        return operation