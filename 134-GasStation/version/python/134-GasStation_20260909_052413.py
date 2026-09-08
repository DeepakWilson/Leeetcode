# Last updated: 9/9/2026, 5:24:13 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        last={}
4        start=0
5        end=0
6        for i in range(len(s)):
7            last[s[i]]=i
8        result=[]
9        for i in range(len(s)):
10            end=max(last[s[i]],end)
11            if i==end:
12                result.append((i-start)+1)
13                start=i+1
14        return result