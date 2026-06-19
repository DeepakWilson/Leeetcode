# Last updated: 6/19/2026, 6:20:14 AM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        s = s[::-1]
4        i = 0
5        # Skip leading spaces (which were trailing spaces before reversing)
6        while i < len(s) and s[i] == " ":
7            i += 1
8        count = 0
9        # Count characters of the first word in the reversed string
10        while i < len(s) and s[i] != " ":
11            count += 1
12            i += 1
13        return count