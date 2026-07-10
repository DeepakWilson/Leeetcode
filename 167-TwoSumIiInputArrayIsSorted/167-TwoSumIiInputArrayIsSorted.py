# Last updated: 7/10/2026, 7:23:02 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k=0
        i=len(numbers)-1
        while(k<i):
            if (numbers[i]+numbers[k]==target):
                return [k+1,i+1]
            elif (numbers[i]+numbers[k]>target):
                i=i-1
            else:
                k+=1

        

