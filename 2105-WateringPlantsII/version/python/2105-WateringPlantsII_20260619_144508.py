# Last updated: 6/19/2026, 2:45:08 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_area = 0
6        while left < right:
7            area = min(height[left], height[right]) * (right - left)
8            if area > max_area:
9                max_area = area
10            if height[left] < height[right]:
11                left += 1
12            else:
13                right -= 1
14        return max_area