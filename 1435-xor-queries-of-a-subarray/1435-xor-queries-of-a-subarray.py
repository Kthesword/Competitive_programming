class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(arr)
        pref = [0] * (n+1)
        for k in range(n):
            pref[k + 1] = pref[k] ^ arr[k]
        ans = [pref[r+1] ^ pref[l] for l, r in queries]
        return ans