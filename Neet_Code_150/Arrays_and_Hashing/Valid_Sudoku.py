'''
Row -> Loop through each row and save each element in a list and if len(list) is same size as len(set(list)) then all elements are unique

Col -> Loop through each column and save each element in a list and if len(list) is same size as len(set(list)) then all elements are unique

Squares -> consider each row and colums of squares as 0,1,2 so total 9 combinations.
Save these (row, col) ((0,0) for first square) as tuple keys to dictionary and values is list of elements in the square, then set the list 
You can divide the row number by 3 and take int to get 0,1,2


'''



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            elements = []
            for j in range(9):
                no = board[i][j]
                if no!= '.':
                    elements.append(no)
            print(elements)
            if len(set(elements)) == len(elements):
                continue
            else:
                return False


        for i in range(9):
            elements = []
            for j in range(9):
                no = board[j][i]
                if no!= '.':
                    elements.append(no)
            print(elements)
            if len(set(elements)) == len(elements):
                continue
            else:
                return False


        new_data = {}
        for i in range(9):
            for j in range(9):
                new_row = int(i/3)
                new_col = int(j/3)

                if board[i][j] != '.':
                    new_data[(new_row, new_col)] = new_data.get((new_row, new_col),[])+[board[i][j]]

            
        # print(new_data)
        for k,v in new_data.items():
            if len(set(v)) == len(v):
                continue
            else:
                return False
        return True 
        

        

        