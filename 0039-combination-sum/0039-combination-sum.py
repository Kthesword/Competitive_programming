class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        ans=[]
        sub=[]
        def bk(idx):
            if idx==len(nums):return 
            if sum(sub)==target and list(sub) not in ans:
                ans.append(list(sub))
                return
            if sum(sub)>target:return
            sub.append(nums[idx])
            bk(idx)
            bk(idx+1)
            sub.pop()
            bk(idx+1)
        bk(0)
        return ans