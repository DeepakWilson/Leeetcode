# Last updated: 6/18/2026, 7:04:30 PM
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        a = num % 9
        if a == 0:
            return 9
        return a