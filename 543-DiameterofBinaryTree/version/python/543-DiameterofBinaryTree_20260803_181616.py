# Last updated: 8/3/2026, 6:16:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        left=self.maxlen(root.left)
12        right=self.maxlen(root.right)
13        diameter=left+right
14        sub=max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
15        return max(diameter, sub)
16
17    def maxlen(self, root: Optional[TreeNode]):
18        if not root:
19            return 0
20        return 1+max(self.maxlen(root.left),self.maxlen(root.right))