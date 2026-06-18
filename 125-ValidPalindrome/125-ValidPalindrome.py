# Last updated: 6/18/2026, 7:04:38 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=[]
        for i in s:
            if i.isalnum():
                new.append(i.lower())
        if new==new[::-1]:
            return True
        else:
            return False