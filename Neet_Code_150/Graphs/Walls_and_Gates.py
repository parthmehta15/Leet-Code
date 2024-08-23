




class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j,0))

        while queue:
            i,j, value = queue.pop(0)
            if i-1>=0:
                if grid[i-1][j] > value:
                    grid[i-1][j] = value + 1
                    queue.append((i-1,j,value+1))
            if j-1>=0:
                if grid[i][j-1] > value:
                    grid[i][j-1] = value + 1
                    queue.append((i,j-1,value+1))

            if i+1<row:
                if grid[i+1][j] > value:
                    grid[i+1][j] = value + 1
                    queue.append((i+1,j,value+1))

            if j+1<col:
                if grid[i][j+1] > value:
                    grid[i][j+1] = value + 1
                    queue.append((i,j+1,value+1))
            
        print(grid)
        