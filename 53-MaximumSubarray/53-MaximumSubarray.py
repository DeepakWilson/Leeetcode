# Last updated: 6/18/2026, 7:04:42 PM
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=0
        max_sum=nums[0] 
        for num in nums:
            current_sum+=num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum<0:
                current_sum =0
        return max_sum