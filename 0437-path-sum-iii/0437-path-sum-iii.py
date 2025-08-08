# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = []
        res = 0
        def dfsmap(node, prefixMap, prefix):
            if not node:
                return

            nonlocal res
            prefix += node.val

            if prefix - targetSum in prefixMap:
                res += prefixMap[prefix - targetSum]
            if prefix in prefixMap:
                prefixMap[prefix] += 1
            else:
                prefixMap[prefix] = 1 

            if node.left:
                dfsmap(node.left, prefixMap.copy(), prefix)
            if node.right:
                dfsmap(node.right, prefixMap.copy(), prefix)
        
        dfsmap(root, {0:1}, 0)
        
        return res      