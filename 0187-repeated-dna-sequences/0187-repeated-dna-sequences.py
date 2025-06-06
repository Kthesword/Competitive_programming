class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # A = 00
        # T = 01
        # C = 10
        # G = 11
        
        res = []
        mp = {"A": 0, "T": 1, "C": 2, "G": 3}
        vis = {}
        ln = len(s)
        
        for i in range(ln-9):
            sequence = 0
            for j in range(i, i+10):
                sequence <<= 2
                sequence |= mp[s[j]]
            
            gt = vis.get(sequence, 0)
            if gt == 1:
                res.append(s[i:i+10])
                vis[sequence] = 2
            elif gt == 0:
                vis[sequence] = 1
                
        return res