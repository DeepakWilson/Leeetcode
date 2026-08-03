# Last updated: 8/3/2026, 9:29:12 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left=0
4        right=len(nums)-1
5        while(left<=right):
6            mid=(right+left)//2
7            if nums[mid]==target:
8                return mid
9            elif nums[mid]>target:
10                right=mid-1
11            else:
12                left=mid+1
13        return -1