# Last updated: 8/10/2026, 1:44:45 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        rev=0
4        sign=-1 if x<0 else 1
5        num=abs(x)
6        while num>0:
7            digit=num%10
8            rev=(rev*10)+digit
9            num=num//10
10        rev=rev*sign
11        if rev<-2**31 or rev>2**31-1:
12             return 0
13        return rev
14        
15        
16
17        