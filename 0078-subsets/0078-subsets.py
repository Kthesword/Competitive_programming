class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # res.append(nums[:])
        def back(k,start,comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for j in range(start,len(nums)):
                comb.append(nums[j])
                back(k,j+1,comb)
                comb.pop()
            comb = []
        k = 1
        for i in range(len(nums)):
            back(k,0,[])
            k += 1
        return res