# Last updated: 8/3/2026, 6:17:11 PM
1class Solution:
2    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
3        self.max_diameter = 0
4        def height(node):
5            if not node:
6                return 0
7            left_height = height(node.left)
8            right_height = height(node.right)
9            self.max_diameter = max(self.max_diameter, left_height + right_height)
10            return 1 + max(left_height, right_height)
11        height(root)
12        return self.max_diameter