class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        left = n

        # find first non-decreasing number
        while left >= 0 and arr[left] >= arr[left-1]:
            left -= 1
            
        # if this hits, it means we have the smallest possible perm 
        if left <= 0:
            return arr
        
        # the while loop above lands us  at +1, so k is the actual value
        k = left - 1
        
        # find the largest number that's smaller than k 
        # while skipping duplicates
        right = n
        while right >= left:
            if arr[right] < arr[k] and arr[right] != arr[right-1]:
                arr[k], arr[right] = arr[right], arr[k]
                return arr
                
            right -= 1
    
        return arr