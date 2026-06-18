# Last updated: 6/18/2026, 7:04:17 PM
class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        new=sorted(nums)
        while low<=high:
            mid=(low+high)//2
            if new[mid]==target:
                return mid
            elif new[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1
