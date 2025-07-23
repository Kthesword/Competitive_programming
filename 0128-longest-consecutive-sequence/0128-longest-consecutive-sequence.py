class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longst = 0
        for n in nset:
            if (n - 1) not in nset: # start of a sequence
                length = 0
                while (n + length) in nset:
                    length += 1
                longst = max(longst, length)

        return longst