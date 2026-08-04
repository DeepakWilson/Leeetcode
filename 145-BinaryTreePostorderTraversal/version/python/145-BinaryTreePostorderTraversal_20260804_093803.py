# Last updated: 8/4/2026, 9:38:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        ret=[]
12        stack=[]
13        while root is not None or stack:
14            while root is not None:
15                stack.append(root)
16                root=root.left
17            root=stack.pop()
18            ret.append(root.val)
19            root=root.right
20        return ret