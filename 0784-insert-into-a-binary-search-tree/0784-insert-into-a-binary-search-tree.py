# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertToBst(node):
            if not node:
                return TreeNode(val)
            if val > node.val:
                node.right = insertToBst(node.right)
            else:
                node.left = insertToBst(node.left)
            return node
        return insertToBst(root)