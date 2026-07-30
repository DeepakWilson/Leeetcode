# Last updated: 7/30/2026, 7:06:25 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        boatcount=0
4        i=0
5        people.sort()
6        j=len(people)-1
7        while(i<=j):
8            if people[i]+people[j]<=limit:
9                i+=1
10            j-=1
11            boatcount+=1
12        return boatcount
13