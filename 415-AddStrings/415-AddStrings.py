# Last updated: 6/18/2026, 7:04:21 PM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=num1[::-1]
        num2=num2[::-1]
        if len(num1)<len(num2):
            num1+='0'*(len(num2)-len(num1))
        else:
            num2+='0'*(len(num1)-len(num2))
        result=""
        carry=0
        for i in range(len(num1)):
            ds=int(num1[i])+int(num2[i])+carry
            carry=ds//10
            result+=str(ds%10)
        if carry>0:
            result+=str(carry)
        return result[::-1]
'''num reverse cheyth...for smaller number add zeroes to th end'''