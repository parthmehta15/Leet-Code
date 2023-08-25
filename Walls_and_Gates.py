class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        def find_gates(rooms):
            gates = set()
            for i in range(len(rooms)):
                for j in range(len(rooms[0])):
                    if rooms[i][j] == 0:
                        gates.add((i,j))

            return gates


        inf = 2147483647
        wall = -1
        m,n = len(rooms), len(rooms[0])
        gates = find_gates(rooms)
        print('gates: ',gates)

        while len(gates)!= 0:
            row, col = gates.pop()
            print('cuur: ', row,col)
            if row+1<m:
                if rooms[row+1][col] > rooms[row][col]:
                    rooms[row+1][col] = rooms[row][col]+1
                    gates.add((row+1,col))

            if col+1<n:
                if rooms[row][col+1] > rooms[row][col]:
                    rooms[row][col+1] = rooms[row][col]+1
                    gates.add((row,col+1))

            if row-1>=0:
                if rooms[row-1][col] > rooms[row][col]:
                    rooms[row-1][col] = rooms[row][col]+1
                    gates.add((row-1,col))
            
            if col-1>=0:
                if rooms[row][col-1] > rooms[row][col]:
                    rooms[row][col-1] = rooms[row][col]+1
                    gates.add((row,col-1))
            
            # print(rooms)