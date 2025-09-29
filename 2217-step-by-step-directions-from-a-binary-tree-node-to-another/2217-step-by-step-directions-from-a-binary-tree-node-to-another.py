# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path1 = []
        path2 = []
        def findVal(root, val, path):
            if not root:
                return False
            if root.val==val:
                return True
            ret = False
            if findVal(root.left, val, path):
                path.append('L')
                ret = True
            elif findVal(root.right, val, path):
                path.append('R')
                ret=True
            return ret
        findVal(root, startValue, path1)
        findVal(root, destValue, path2)
        ret = []
        i = 0
        print(path1, path2)
        while 0<=i<len(path1) and 0<=i<len(path2) and path1[-1-i]==path2[-1-i]:
            i+=1
        for j in range(len(path1)-i):
            ret.append('U')
        for j in range(len(path2)-i-1, -1, -1):
            ret.append(path2[j])
        return ''.join(ret)
