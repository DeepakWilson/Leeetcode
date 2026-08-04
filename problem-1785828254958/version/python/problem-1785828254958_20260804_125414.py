# Last updated: 8/4/2026, 12:54:14 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced=[True]
10        def height(root):
11            if not root:
12                return 0
13            left=height(root.left)
14            right=height(root.right)
15            if abs(right-left)>1:
16                balanced[0]= False
17                return 0
18            return 1+ max(left,right)
19        height(root)
20        return balanced[0]