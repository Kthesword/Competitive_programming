class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            cnt = 0
            while num:
                
                cnt += num & (1 << 0) != 0
                num = num >> 1

            ans.append(cnt)
        return ans
