# Last updated: 7/30/2026, 7:06:53 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while (left<right):
            mid=(left+right)//2
            sum=0
            for i in nums:
                sum+=ceil(i/mid)
            if sum<=threshold: 
                right=mid
            else:
                left=mid+1
        return left 
