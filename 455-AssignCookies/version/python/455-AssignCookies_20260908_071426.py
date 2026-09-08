# Last updated: 9/8/2026, 7:14:26 AM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        g.sort()
4        s.sort()
5        i=j=0
6        while i<len(g) and j<len(s):
7            if s[j]>=g[i]:
8                i+=1
9            j+=1
10        return i