# Last updated: 8/3/2026, 7:20:48 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3       mydict={}
4       for i in nums:
5          if i in mydict:
6             mydict[i]+=1
7          else:
8            mydict[i]=1
9       for i in mydict:
10        if mydict[i]==1:
11            return i
12        
13    
14       
15    