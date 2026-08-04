# Last updated: 8/4/2026, 9:45:34 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        ret=[]
12        from collections import deque
13        queue=deque([root])
14        while queue:
15            ret_row=[]
16            for _ in range(len(queue)):
17                node=queue.popleft()
18                ret_row.append(node.val)
19                if node.left:
20                    queue.append(node.left)
21                if node.right:
22                    queue.append(node.right)
23            ret.append(ret_row)
24        return ret
25