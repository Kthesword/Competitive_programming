class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        counter = Counter([x % k for x in arr])
        for rem in counter:
            if rem == 0:
                if counter[rem] % 2 != 0:
                    return False
            else:
                if counter[rem] != counter[k-rem]:
                    return False
        
        return True
            