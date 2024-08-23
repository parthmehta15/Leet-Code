#Using 2 binary searches -> one to select the row and one to search within the row
#Almost same as 2nd solution just manually writing code for binary search
#Finidng the row which the number can be in so binary search to find row -> log m
#Then doing another binary search column wise to see if element exists -> log n
# logm + logn -> logmn
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_cols = len(matrix[0])

        top = 0
        bottom = n_row -1

        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target >  matrix[mid_row][-1]:
                top =  mid_row + 1
            else:
                break

        if top > bottom:
            return False
        
        left = 0
        right = n_cols - 1
        while left <= right:
            mid = (left + right) //2
            if matrix[mid_row][mid] < target:
                left = mid +1 
            elif matrix[mid_row][mid] > target:
                right = mid - 1
            elif matrix[mid_row][mid] == target:
                return True
        return False
        






# #Using python in-built functions - faster and less memory
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         master_data = []
#         for i in matrix:
#             master_data += i
#         if target in master_data:
#             return True
#         else:
#             return False
        
        


# # Using numpy - slow and more memory
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         import numpy as np
#         matrix = np.array(matrix)
#         matrix = matrix.reshape(-1)
#         if target in matrix:
#             return True
#         else:
#             return False
        
        