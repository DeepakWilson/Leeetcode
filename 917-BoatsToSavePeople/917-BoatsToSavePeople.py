# Last updated: 7/30/2026, 7:06:55 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatcount=0
        i=0
        people.sort()
        j=len(people)-1
        while(i<=j):
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            boatcount+=1
        return boatcount
