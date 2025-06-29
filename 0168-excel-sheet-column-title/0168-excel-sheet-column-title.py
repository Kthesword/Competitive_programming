class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def excel(n, c):
            if n < 1:
                return c
            c += chr((n - 1)%26 + ord("A"))
            n = (n - 1) // 26
            return excel(n, c)
        
        return excel(columnNumber, "")[::-1]
        

            

