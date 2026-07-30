# Last updated: 7/30/2026, 7:06:59 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            sum=0
            for i in piles:
                sum+=ceil(i/mid)
            if sum<=h:
                right=mid
            else:
                left= mid+1
        return right

        