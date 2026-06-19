# Last updated: 6/19/2026, 10:23:45 AM
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        waterA=capacityA
        waterB=capacityB
        count=0
        k=0
        i=len(plants)-1
        while(k<i):
            if waterA<plants[k]:
                waterA=capacityA
                count+=1
            waterA-=plants[k]
            k+=1
            if waterB<plants[i]:
                waterB=capacityB
                count+=1
            waterB-=plants[i]
            i-=1
        if k==i:
          if max(waterA,waterB)<plants[i]:
             count+=1
        return count
            
