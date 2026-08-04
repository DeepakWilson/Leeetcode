# Last updated: 8/4/2026, 2:36:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=[True]
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            if abs(right-left)>1:
                balanced[0]= False
                return 0
            return 1+ max(left,right)
        height(root)
        return balanced[0]