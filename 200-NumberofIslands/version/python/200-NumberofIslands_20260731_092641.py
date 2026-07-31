# Last updated: 7/31/2026, 9:26:41 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        m=len(grid)
4        n=len(grid[0])
5        island=0
6        def dfs(i,j):
7            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
8                return
9            else:
10                grid[i][j]='0'
11                dfs(i,j+1)
12                dfs(i,j-1)
13                dfs(i+1,j)
14                dfs(i-1,j)
15        for i in range(m):
16            for j in range(n):
17                if grid[i][j]=='1':
18                    island+=1
19                    dfs(i,j)
20        return island