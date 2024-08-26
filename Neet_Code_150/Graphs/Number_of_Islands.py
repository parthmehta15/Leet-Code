'''

Iterate through all elements in grid, if '1' encountered and not visited then run seperate bfs on it.
Can also shift the bfs code to a fucntion 

'''




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        visited = set()

        row = len(grid)
        col = len(grid[0])

        n_islands = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    n_islands += 1
                    #DO BFS
                    queue = []
                    queue.append((i,j))
                    visited.add((i,j))
                    while queue:
                        r,c = queue.pop(0)
                        if r+1 < row:
                            if grid[r+1][c] == '1' and (r+1,c) not in visited:
                                queue.append((r+1,c))
                                visited.add((r+1,c))

                        if c-1 >= 0:
                            if grid[r][c-1] == '1' and (r,c-1) not in visited:
                                queue.append((r,c-1))
                                visited.add((r,c-1))

                        if c+1 < col:
                            if grid[r][c+1] == '1' and (r,c+1) not in visited:
                                queue.append((r,c+1))
                                visited.add((r,c+1))

                        if r-1 >= 0 :
                            if grid[r-1][c] == '1' and (r-1,c) not in visited:
                                queue.append((r-1,c))
                                visited.add((r-1,c))
                

        return n_islands