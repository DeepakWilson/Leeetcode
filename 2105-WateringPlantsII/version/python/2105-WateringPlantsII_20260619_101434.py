# Last updated: 6/19/2026, 10:14:34 AM
1class Solution:
2    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
3        waterA=capacityA
4        waterB=capacityB
5        count=0
6        k=0
7        i=len(plants)-1
8        while(k<i):
9            if waterA<plants[k]:
10                waterA=capacityA
11                count+=1
12            waterA-=plants[k]
13            k+=1
14            if waterB<plants[i]:
15                waterB=capacityB
16                count+=1
17            waterB-=plants[i]
18            i-=1
19        if k==i:
20          if max(waterA,waterB)<plants[i]:
21             count+=1
22        return count
23            
24