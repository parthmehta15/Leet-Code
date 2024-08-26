
'''
Lop through all elements in grid, if value 1 and not in visited, apply bfs on that.
can use function for that code
Keep track of curr_area and max_area

Max_area kept track of using a list to reference it within function 


'''



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = [0]
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        def bfs(i,j):
            queue = []
            queue.append((i,j))
            visited.add((i,j))
            curr_area = 1

            while queue:

                r,c = queue.pop(0)
                if r+1<rows:
                    if grid[r+1][c] == 1 and (r+1,c) not in visited:
                        queue.append((r+1,c))
                        visited.add((r+1,c))
                        curr_area = curr_area + 1

                if r-1>=0:
                    if grid[r-1][c] == 1 and (r-1,c) not in visited:
                        queue.append((r-1,c))
                        visited.add((r-1,c))
                        curr_area = curr_area + 1

                if c+1<cols:
                    if grid[r][c+1] == 1 and (r,c+1) not in visited:
                        queue.append((r,c+1))
                        visited.add((r,c+1))
                        curr_area = curr_area + 1

                if c-1>=0:
                    if grid[r][c-1] == 1 and (r,c-1) not in visited:
                        queue.append((r,c-1))
                        visited.add((r,c-1))
                        curr_area = curr_area + 1

            max_area[0] = max(max_area[0], curr_area)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:

                    #Apply BFS on (i,j)
                    bfs(i, j)
        
        return max_area[0]