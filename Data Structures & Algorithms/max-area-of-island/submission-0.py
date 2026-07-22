class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (not((i,j) in visited)):
                    area = 0
                    currentArea = self.findArea(i,j,grid,visited,area)
                    print(currentArea)
                    if maxArea < currentArea:
                        maxArea = currentArea
        return maxArea

    def findArea(self,i,j,grid,visited,area):
        if (i<0 or j<0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0 or ((i,j) in visited)):
            visited.add((i,j))
            return area
        
        area = area + 1    
        visited.add((i,j))
        area = self.findArea(i+1,j,grid,visited,area)
        area = self.findArea(i-1,j,grid,visited,area)
        area = self.findArea(i,j+1,grid,visited,area)
        area = self.findArea(i,j-1,grid,visited,area)
        return area