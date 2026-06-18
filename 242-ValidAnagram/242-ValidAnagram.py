# Last updated: 6/18/2026, 7:04:31 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=0
        if(len(s)!=len(t)):
            return False
        s1=sorted(s)
        t1=sorted(t)
        for i in range(len(s1)):
            if s1[i]!=t1[i]:
                return False
        return True
        