# Last updated: 9/9/2026, 6:37:31 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        limit=0
4        for i in range(len(nums)):
5            if i>limit:
6                return False
7            limit=max(limit,i+nums[i])
8        return True