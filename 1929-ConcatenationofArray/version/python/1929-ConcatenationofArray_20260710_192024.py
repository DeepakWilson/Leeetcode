# Last updated: 7/10/2026, 7:20:24 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        res=[]
4        for i in range(2*(len(nums))):
5            if i>=len(nums):
6                res.append(nums[i-len(nums)])
7            else:
8                res.append(nums[i])
9        return res