# Last updated: 7/25/2026, 10:58:38 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        if len(s1)>len(s2):
4            return False
5        for left in range(len(s2)-len(s1)+1):
6            window=s2[left:left+len(s1)]
7            if sorted(window)==sorted(s1):
8                return True
9        return False