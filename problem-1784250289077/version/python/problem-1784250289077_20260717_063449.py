# Last updated: 7/17/2026, 6:34:49 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        left=[1]*len(nums)
4        answer=[1]*len(nums)
5        right=[1]*len(nums)
6        left[0]=1
7        for i in range(1,len(nums)):
8            left[i]=left[i-1]*nums[i-1]
9        right[len(nums)-1]=1
10        for i in range(len(nums)-2,-1,-1):
11            right[i]=right[i+1]*nums[i+1]
12        for i in range(len(nums)):
13            answer[i]=left[i]*right[i]
14        return answer