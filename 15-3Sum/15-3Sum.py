# Last updated: 7/28/2026, 11:00:48 AM
1class Solution:
2
3  def threeSum(self, nums: list[int]) -> list[list[int]]:
4    nums.sort()
5    res = []
6    n = len(nums)
7
8    for i in range(n):
9      # Optimization: If the current number is > 0, the remaining numbers 
10      # are also positive, meaning their sum can never be 0.
11      if nums[i] > 0:
12        break
13
14      if i > 0 and nums[i] == nums[i - 1]:
15        continue
16
17      left, right = i + 1, n - 1
18      while left < right:
19        currentsum = nums[i] + nums[left] + nums[right]
20
21        if currentsum == 0:
22          res.append([nums[i], nums[left], nums[right]])
23          while left < right and nums[left] == nums[left + 1]:
24            left += 1
25          while left < right and nums[right] == nums[right - 1]:
26            right -= 1
27          left += 1
28          right -= 1
29        elif currentsum < 0:
30          left += 1
31        else:
32          right -= 1
33
34    return res