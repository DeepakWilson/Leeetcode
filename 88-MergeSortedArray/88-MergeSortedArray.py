# Last updated: 6/19/2026, 5:40:43 AM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[k]
            k=k+1
        nums1.sort()




        