class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # list of the sneaky numbers
        sneaky = []
        # a set to check if number occurs again
        hash = set()
        # find the sneaky numbers
        for num in nums:
            if num in hash:
                sneaky.append(num)
            else:
                hash.add(num)
        
        return sneaky
