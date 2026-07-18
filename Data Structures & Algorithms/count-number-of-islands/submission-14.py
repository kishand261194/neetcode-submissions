class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        noOfIslands = 0
        for i in range (0, len(grid)):
            for j in range (0, len(grid[i])):
                if ((i,j) not in visited):
                    noOfIslands = noOfIslands + self.lookup(i, j, grid, visited)
        return noOfIslands

    def lookup(self, i, j, grid, visited):
        if ((i,j) in visited):
            return 0
        if (i >= len(grid) or j >= len(grid[i]) or i < 0 or j < 0 or grid[i][j] == "0"):
            return 0
        visited.add((i,j))
        self.lookup(i+1,j,grid,visited)
        self.lookup(i-1,j,grid,visited)
        self.lookup(i,j-1,grid,visited)
        self.lookup(i,j+1,grid,visited) 
        return 1