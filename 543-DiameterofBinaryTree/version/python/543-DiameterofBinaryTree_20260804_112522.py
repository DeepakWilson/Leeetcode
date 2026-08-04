# Last updated: 8/4/2026, 11:25:22 AM
1class Solution:
2    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
3        max_diameter=[0]
4        def height(root):
5            if not root:
6                return 0
7            left=height(root.left)
8            right=height(root.right)
9            diameter=left+right
10            max_diameter[0]=max(max_diameter[0],diameter)
11            return 1+max(left,right)
12        height(root)
13        return max_diameter[0]