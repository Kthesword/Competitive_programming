#in the name of Allah
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        h = x
        if len(str(x)) == 1:
            return True
        elif x*-1 == abs(x):
            return False
        else:
            while x != 0:
                b = len(str(x)) - 1
                t  = x % 10
                ans += t * 10**(b)
                x //= 10
        return ans == h