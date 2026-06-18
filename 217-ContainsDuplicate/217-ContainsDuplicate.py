# Last updated: 6/18/2026, 7:04:33 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #mymethod
        '''nums.sort()
        for i in range(len(nums)-1):
                if (nums[i]==nums[i+1]):
                    return True
        return False
        ''' 
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False       
        