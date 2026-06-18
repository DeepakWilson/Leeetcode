# Last updated: 6/18/2026, 7:04:50 PM
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                   return [i,j]
        
            