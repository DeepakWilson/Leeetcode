# Last updated: 7/26/2026, 7:13:31 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        for left in range(len(s2)-len(s1)+1):
            window=s2[left:left+len(s1)]
            if sorted(window)==sorted(s1):
                return True
        return False