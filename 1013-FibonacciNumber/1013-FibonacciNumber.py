# Last updated: 6/18/2026, 7:04:11 PM
class Solution(object):
    def fib(self, n):
        a=0
        b=1
        if n==0:
            return a
        elif n==1:
            return b
        else:
            for i in range (n-1):
                c=a+b
                a=b
                b=c
            return c
        