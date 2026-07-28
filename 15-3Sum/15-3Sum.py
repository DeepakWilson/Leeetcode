# Last updated: 7/28/2026, 11:00:10 AM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        res=[]
5        for i in range(len(nums)):
6            if i>0 and nums[i]==nums[i-1]:
7                continue
8            left=i+1
9            right=len(nums)-1
10            while(left<right):
11                currentsum=nums[i]+nums[left]+nums[right]
12                if currentsum==0:
13                    res.append([nums[i],nums[left],nums[right]])
14                    while left<right and nums[left]== nums[left+1]:
15                        left+=1
16                    while left<right and nums[right]==nums[right-1]:
17                        right-=1
18                    left+=1
19                    right-=1                
20                elif currentsum<0:
21                    left+=1
22                else:
23                    right-=1
24        return res