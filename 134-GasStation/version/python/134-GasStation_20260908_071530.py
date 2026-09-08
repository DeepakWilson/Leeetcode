# Last updated: 9/8/2026, 7:15:30 AM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        start=0
4        total=0
5        tank=0
6        for i in range (len(gas)):
7            total+=gas[i]-cost[i]
8            tank+=gas[i]-cost[i]
9            if tank<0:
10                start=i+1
11                tank=0
12        if total>=0:
13            return start
14        else:
15            return -1
16