# Last updated: 6/18/2026, 7:04:46 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        pal=0
        while a>0:
            digit=a%10
            pal=pal*10+digit
            a=a//10
        if pal==x:
            return True
        else:
            return False

