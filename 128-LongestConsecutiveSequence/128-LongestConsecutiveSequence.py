# Last updated: 7/28/2026, 9:55:51 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3     length=0
4     maxlen=0
5     seen=set(nums)
6     for i in seen:
7        if (i-1) not in seen:
8            length=1
9            while (i+length) in seen:
10                length+=1
11            maxlen=max(length, maxlen)
12     return maxlen
13