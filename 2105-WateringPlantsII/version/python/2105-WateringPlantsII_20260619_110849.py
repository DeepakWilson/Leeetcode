# Last updated: 6/19/2026, 11:08:49 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        k=0
4        i=len(numbers)-1
5        while(k<i):
6            if (numbers[i]+numbers[k]==target):
7                return [k+1,i+1]
8            elif (numbers[i]+numbers[k]>target):
9                i=i-1
10            else:
11                k+=1
12
13        
14
15