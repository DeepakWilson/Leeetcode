# Last updated: 7/30/2026, 2:46:11 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        left=1
4        right=max(nums)
5        while (left<right):
6            mid=(left+right)//2
7            sum=0
8            for i in nums:
9                sum+=ceil(i/mid)
10            if sum<=threshold: 
11                right=mid
12            else:
13                left=mid+1
14        return left 
15