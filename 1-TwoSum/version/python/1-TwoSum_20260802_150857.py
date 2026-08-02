# Last updated: 8/2/2026, 3:08:57 PM
1class Solution(object):
2    def twoSum(self, nums, target):
3        num_map={}
4        for i in range(len(nums)):
5            num=nums[i]
6            complement=target-num
7            if complement in num_map:
8                return [num_map[complement],i]
9            num_map[num]=i
10        
11            