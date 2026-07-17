# Last updated: 7/17/2026, 6:36:26 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        answer=[1]*len(nums)
        right=[1]*len(nums)
        left[0]=1
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        right[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(len(nums)):
            answer[i]=left[i]*right[i]
        return answer