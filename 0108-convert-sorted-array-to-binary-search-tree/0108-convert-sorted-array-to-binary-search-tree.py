# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def setval(li):
            if not li:
                return None
            r = len(li) - 1
            mid = r // 2
            node = TreeNode()
            node.val = li[mid]
            node.left = setval(li[:mid])
            node.right = setval(li[mid+1:])
            return node

        return setval(nums)


            


            
