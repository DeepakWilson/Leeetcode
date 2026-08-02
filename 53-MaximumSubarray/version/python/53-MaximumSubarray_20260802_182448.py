# Last updated: 8/2/2026, 6:24:48 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        currentsum=0
4        maxsum=nums[0]
5        for num in nums:
6            currentsum+=num
7            maxsum=max(currentsum, maxsum) 
8            if currentsum<0:
9                currentsum=0
10        return maxsum