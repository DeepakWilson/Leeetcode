# Last updated: 6/18/2026, 7:04:36 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans
       
