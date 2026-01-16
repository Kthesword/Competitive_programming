class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        if not n or n == 1 and nums[-1] == val:
            return 0
        if n == 1 and nums[-1] != val:
            return 1
        l, r = 0, n-1
        k = 0
        c = nums.count(val)
        while l < r:
            if nums[l] == val:
                while r > l and nums[r] == val:
                    r -= 1
                nums[l] = nums[r]
                nums[r] = val
        
            l += 1
        while nums and nums[-1] == val:
            nums.pop()
        return n - k

        
                





        # que = deque()
        # r = []
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == val:
        #         count += 1
        #         que.append(i)
        #     else:
        #         if count < 0:
        #             r.append(i)
        #         count -= 1
                
        # while que and r:
        #     left = que.popleft()
        #     i = r.pop()
        #     print(nums[left], "i", nums[i])
        #     nums[left], nums[i] = nums[i], nums[left]
        # print(que)
        # return n - count