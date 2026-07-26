# Last updated: 7/26/2026, 7:09:58 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        mydict={}
4        for i in nums:
5            if i in mydict:
6                mydict[i]+=1
7            else:
8                mydict[i]=1
9        new=sorted(mydict, key=mydict.get, reverse=True)
10        return new[:k]