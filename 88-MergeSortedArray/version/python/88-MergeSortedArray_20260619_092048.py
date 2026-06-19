# Last updated: 6/19/2026, 9:20:48 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        k=0
4        for i in range(m,len(nums1)):
5            nums1[i]=nums2[k]
6            k=k+1
7        nums1.sort()
8#2 pointer approach???
9
10
11
12        