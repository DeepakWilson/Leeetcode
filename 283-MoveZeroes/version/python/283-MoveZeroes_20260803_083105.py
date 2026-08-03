# Last updated: 8/3/2026, 8:31:05 AM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        nonzero=[]
4        for i in range(len(nums)):
5            if nums[i]!=0:
6                nonzero.append(nums[i])
7        while(len(nums)>len(nonzero)):
8            nonzero.append(0)
9        nums[:]=nonzero
10                
11
12        