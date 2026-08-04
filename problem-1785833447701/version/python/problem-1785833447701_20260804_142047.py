# Last updated: 8/4/2026, 2:20:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        def balanced(p,q):
10            if not p and not q:
11                return True
12            if (p and not q) or (not p and q):
13                return False
14            if (p.val!=q.val):
15                return False
16            return balanced(p.left, q.left) and balanced(p.right, q.right)
17        return balanced(p,q)
18