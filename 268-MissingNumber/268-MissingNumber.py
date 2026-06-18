# Last updated: 6/18/2026, 7:04:28 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
        
            