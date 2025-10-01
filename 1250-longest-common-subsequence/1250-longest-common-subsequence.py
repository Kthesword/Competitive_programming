class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat=[ [ 0 for i in range(len(text1)+1) ] for j in range(len(text2)+1) ]
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                if text2[i-1]==text1[j-1]:
                    mat[i][j]=1+mat[i-1][j-1]
                else:
                    mat[i][j]=max(mat[i-1][j],mat[i][j-1])
        return mat[len(text2)][len(text1)]

