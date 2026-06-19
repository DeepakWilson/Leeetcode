# Last updated: 6/19/2026, 6:24:40 AM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s=s[::-1]
4        i=0
5        count=0
6        while i<len(s) and s[i]==" ":
7            i=i+1
8        while i<len(s) and s[i]!=" ":
9            count=count+1
10            i=i+1
11        return count