

'''
Think in reverse: (DFS)
So find all locatins onborder which are O and then add then to a STACK and to visited set.
Now check adjoining elements if they are also O then add to stack and visited.

In the end change all X except at position in visited



'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        rows= len(board)
        cols = len(board[0])
                    
                
        visited = set()
        stack = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1:
                    if board[i][j] == 'O' and (i,j) not in stack:
                        stack.append((i,j))
                if j == 0 or j == cols-1:
                    if board[i][j] == 'O' and (i,j) not in stack:
                        stack.append((i,j))

        
        while stack:
            r,c = stack.pop()
            visited.add((r,c))
            
            if r-1>0:
                if board[r-1][c] == 'O' and ((r-1,c)) not in visited:
                    stack.append((r-1,c))
                    visited.add((r-1,c))
            if r+1<rows:
                if board[r+1][c] == 'O' and ((r+1,c)) not in visited:
                    stack.append((r+1,c))
                    visited.add((r+1,c))
            if c-1>0:
                if board[r][c-1] == 'O' and ((r,c-1)) not in visited:
                    stack.append((r,c-1))
                    visited.add((r,c-1))

            if c+1<cols:
                if board[r][c+1] == 'O' and ((r,c+1)) not in visited:
                    stack.append((r,c+1))
                    visited.add((r,c+1))

        for i in range(rows):
            for j in range(cols):
                if (i,j) in visited:
                    continue
                else:
                    board[i][j] = 'X'

   
        