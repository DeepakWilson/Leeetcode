# Last updated: 6/18/2026, 7:04:24 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique=set()
        for num in nums1:
            if num in nums2:
                unique.add(num)
        return list(unique)
                
