# Last updated: 6/18/2026, 7:04:40 PM
class Solution(object):
    def climbStairs(self, n):
        a=1
        b=2
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range (3,n+1):
                c=a+b
                a=b
                b=c
            return c

        