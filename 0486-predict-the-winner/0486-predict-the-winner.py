class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def predict(i, j, check):
            if i > j:
                return 0
            best = 0
            if check:
                best = predict(i + 1, j, False) + nums[i]
                best = max(best, predict(i, j - 1, False)+ nums[j]) 

            else:
                best = predict(i + 1, j, True) - nums[i]
                best = min(best, predict(i, j - 1, True)- nums[j]) 
                
            return best

        return predict(0, len(nums) - 1, True) >= 0
        