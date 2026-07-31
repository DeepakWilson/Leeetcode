# Last updated: 7/31/2026, 10:25:30 AM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        m=len(image)#rows
4        n=len(image[0])#columns
5        start_color= image[sr][sc]
6        if color==start_color:
7            return image
8        def dfs(i,j):
9            if i<0 or i>=m or j<0 or j>=n or image[i][j]!=start_color:
10                return
11            else:
12                image[i][j]= color
13                dfs(i,j+1)
14                dfs(i,j-1)
15                dfs(i+1,j)
16                dfs(i-1,j)
17        dfs(sr,sc)
18        return image
19            
20