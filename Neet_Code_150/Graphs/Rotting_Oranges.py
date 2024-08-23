
'''
Find all fresh and total oranges, if fresh = 0 return 0 (edge case)
assign queue, visited set
Use BFS
Have loop for len of queue in while loop and increase time after each loop (If you increase beofre then return time-1)

If len(visited) = total oranges then return time else return -1 (You can skip the visited set if you reduce count of fresh oranges and if zero than return time)




'''



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        total_oranges = 0
        fresh_oranges = 0

        visited = set()
        queue = []

        #Find all rotten oranges and total numnber of oranges 
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    total_oranges += 1
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    total_oranges += 1
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        total_time = 0 #Number of passes through queue
        while queue:
            total_time += 1
            queue_len = len(queue)

            for q in range(queue_len):
                i,j = queue.pop(0)

                if i-1>=0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    visited.add((i-1,j))
                    queue.append((i-1,j))
                    

                if i+1<n_rows and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    visited.add((i+1,j))
                    queue.append((i+1,j))
                
                if j-1>=0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    visited.add((i,j-1))
                    queue.append((i,j-1))

                if j+1<n_cols and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    visited.add((i,j+1))
                    queue.append((i,j+1))

        if total_oranges == len(visited):
            return total_time-1
        else:
            return -1
                
        
        