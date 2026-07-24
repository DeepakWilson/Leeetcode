# Last updated: 7/24/2026, 6:34:59 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left=0
4        max_len=0
5        seen=set()
6        for right in range(len(s)):
7            while s[right] in seen:
8                seen.remove(s[left])
9                left+=1
10            seen.add(s[right])
11            max_len=max(max_len,right-left+1)
12        return max_len
13