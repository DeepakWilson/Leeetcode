# Last updated: 6/18/2026, 7:04:34 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]>(len(nums))//2:
                return i