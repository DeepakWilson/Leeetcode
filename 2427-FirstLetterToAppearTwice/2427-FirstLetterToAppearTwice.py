# Last updated: 6/18/2026, 7:04:12 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set()
        for i in s:
            if i in seen:
                return i
            else:
                seen.add(i)

            