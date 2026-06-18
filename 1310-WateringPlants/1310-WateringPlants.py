# Last updated: 6/18/2026, 7:04:14 PM
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        water=capacity
        for i in range(len(plants)):
            if water<plants[i]:
                water=capacity
                steps=steps+ 2*i
            steps=steps+1
            water=water-plants[i]
        return steps


            