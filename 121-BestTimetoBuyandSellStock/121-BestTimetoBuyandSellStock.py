# Last updated: 7/24/2026, 6:21:48 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        smallest=prices[0]
4        max_profit=0
5        for i in range(1,len(prices)):
6            smallest=min(smallest,prices[i])
7            max_profit=max(max_profit,prices[i]-smallest)
8        return max_profit
9
10