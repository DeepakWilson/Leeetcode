# Last updated: 6/19/2026, 2:44:12 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        ans=0
4        for i in nums:
5            ans^=i
6        return ans
7       
8