# Last updated: 7/30/2026, 12:33:01 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        left=1
4        right=max(piles)
5        while left<right:
6            mid=(left+right)//2
7            sum=0
8            for i in piles:
9                sum+=ceil(i/mid)
10            if sum<=h:
11                right=mid
12            else:
13                left= mid+1
14        return right
15
16        