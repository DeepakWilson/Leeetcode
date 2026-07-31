# Last updated: 7/31/2026, 10:26:53 AM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)#rows
        n=len(image[0])#columns
        start_color= image[sr][sc]
        if color==start_color:
            return image
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or image[i][j]!=start_color:
                return
            else:
                image[i][j]= color
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)
        dfs(sr,sc)
        return image
            
