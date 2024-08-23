'''
USE DFS RECURIOSN 

Define another funtion to find height of tree -> same as maximum_depth_of_binary_tree,
Only difference in updating value of diameter inside the loop


Other difference is updating height in the return statement '+1'.

#Update Diameter
#Saving in list to save to memory location otherwise can use 
# 'nonlocal diameter'


'''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        diameter = [0]
        def depth_dfs(node_):

            #Base Case
            if node_ == None:
                return 0

            #Left
            left = depth_dfs(node_.left)

            #Right
            right = depth_dfs(node_.right)
            
            diameter[0] = max(diameter[0], left + right) #Update Diameter
            #Saving in list to save to memory location otherwise can use 
            # 'nonlocal diameter'

            return 1 + max(left, right) # Return Max Height
        
        depth_dfs(root)

        return diameter[0]