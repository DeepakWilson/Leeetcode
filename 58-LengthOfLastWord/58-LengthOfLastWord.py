# Last updated: 6/19/2026, 10:24:23 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        i=0
        count=0
        while i<len(s) and s[i]==" ":
            i=i+1
        while i<len(s) and s[i]!=" ":
            count=count+1
            i=i+1
        return count