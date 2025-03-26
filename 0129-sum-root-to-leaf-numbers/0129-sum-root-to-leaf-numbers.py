# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, curr_path):
            if not node:
                return
            curr_path += str(node.val)
            if not node.left and not node.right:
                res.append(int(curr_path))
            else:
                dfs(node.left, curr_path)
                dfs(node.right, curr_path)

        dfs(root, "")
        
        return sum(res)
