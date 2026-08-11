# Last updated: 8/11/2026, 6:09:09 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        '''k=0
4        for i in range(len(nums)):
5            if nums[i]!=val:
6                nums[k]=nums[i]
7                k+=1
8        return k
9        '''
10        new=[]
11        for i in range(len(nums)):
12            if nums[i]!=val:
13                new.append(nums[i])
14        nums[:]=new
15        return len(new)
16        