class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [-1]*len(s)
        def countWays(i):
            if i == len(s):
                return 1
            if mem[i]!=-1:
                return mem[i]
            if s[i] == '0':
                return 0
            if i == len(s)-1:
                return 1
            if  int(s[i:i+2])<=26:
                mem[i] =  countWays(i+1) + countWays(i+2)
            else:
                mem[i] = countWays(i+1)
            return mem[i]

        return countWays(0)