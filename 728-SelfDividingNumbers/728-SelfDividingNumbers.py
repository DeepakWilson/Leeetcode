# Last updated: 6/18/2026, 7:04:18 PM
class Solution(object):
    def selfDividingNumbers(self, left, right):
        sd=[]
        for i in range(left,right+1):
            flag=1
            a=i
            while(i>0):
                digit=i%10
                if digit==0:
                    flag=1
                    break
                if a%digit==0:
                    flag=0
                else:
                    flag=1
                    break
                i=i//10
            if flag==0:
                sd.append(a)
        return sd

        