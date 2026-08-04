# Last updated: 8/4/2026, 10:59:29 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret=[]
        stack=[]
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root=root.left
            root=stack.pop()
            ret.append(root.val)
            root=root.right
        return ret