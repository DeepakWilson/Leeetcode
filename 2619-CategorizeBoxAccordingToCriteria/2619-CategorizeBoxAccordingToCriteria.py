# Last updated: 6/18/2026, 7:04:15 PM
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol=length*width*height
        flag1=0
        flag2=0
        if length>=10**4 or width>=10**4 or height>=10**4 or vol>=10**9:
            flag1=1
        if mass>=100:
            flag2=1
        if flag1==1 and flag2==1:
            return "Both"
        elif flag1==1 and flag2==0:
            return "Bulky"
        elif flag1==0 and flag2==1:
            return "Heavy"
        else:
            return "Neither"
        
    
        
        