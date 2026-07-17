# Last updated: 7/17/2026, 6:33:42 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        left=[1]*n
5        answer=[1]*n
6        right=[1]*n
7        left[0]=1
8        for i in range(1,n):
9            left[i]=left[i-1]*nums[i-1]
10        right[n-1]=1
11        for i in range(n-2,-1,-1):
12            right[i]=right[i+1]*nums[i+1]
13        for i in range(n):
14            answer[i]=left[i]*right[i]
15        return answer