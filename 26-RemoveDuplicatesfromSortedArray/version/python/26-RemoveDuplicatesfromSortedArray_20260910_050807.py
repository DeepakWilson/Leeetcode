# Last updated: 9/10/2026, 5:08:07 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        new=[]
4        for i in nums:
5            if i not in new:
6                new.append(i)
7        nums[:]=new
8
9
10        