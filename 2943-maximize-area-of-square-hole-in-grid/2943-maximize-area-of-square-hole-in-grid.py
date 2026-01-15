class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:        
        def longest_consecutive(arr):
            if not arr:
                return 0
            arr.sort()
            longest = curr = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 1
            return longest

        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)

        side = min(max_h + 1, max_v + 1)
        return side * side
