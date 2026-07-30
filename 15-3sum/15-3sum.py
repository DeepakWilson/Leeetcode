# Last updated: 7/30/2026, 7:07:56 PM
class Solution:

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n):
      # Optimization: If the current number is > 0, the remaining numbers 
      # are also positive, meaning their sum can never be 0.
      if nums[i] > 0:
        break

      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, n - 1
      while left < right:
        currentsum = nums[i] + nums[left] + nums[right]

        if currentsum == 0:
          res.append([nums[i], nums[left], nums[right]])
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1
          left += 1
          right -= 1
        elif currentsum < 0:
          left += 1
        else:
          right -= 1

    return res