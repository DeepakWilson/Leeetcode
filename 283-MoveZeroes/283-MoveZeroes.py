# Last updated: 6/18/2026, 7:04:27 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                nonzero.append(nums[i])
        while(len(nums)>len(nonzero)):
            nonzero.append(0)
        nums[:]=nonzero
                

        