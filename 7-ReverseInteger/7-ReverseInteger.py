# Last updated: 6/18/2026, 7:04:48 PM
class Solution(object):
    def reverse(self, x):
        y = x
        if x < 0:
            y = -x
        rev = 0
        while y>0:
            digit = y % 10
            rev = rev * 10 + digit
            y //= 10
        if x < 0:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev