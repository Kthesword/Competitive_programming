class Solution:
    def printVertically(self, s: str) -> List[str]:
        ls = s.strip().split()   #convert string to list
        rls = []    # List to store the returned values
        o = 0       
        ix = 0       #index of characters in the list

        # the while loop accumulates words from the inner loop to the returned list
        while o < max([len(u) for u in ls]): 
            wrd = ""
            
            #collects characters of converted string iterating over the first list
            for i in range(len(ls)): 
                if ix >= len(ls[i]):   #avoid index out of range
                    wrd += " "
                else: 
                    wrd += ls[i][ix]
            ix += 1
            lwr = [c for c in wrd]
            while lwr[-1] == " ": #Avoid trailing spaces
                lwr.pop()
            wrd = "".join(lwr)
            rls.append(wrd)
            o += 1
        return rls