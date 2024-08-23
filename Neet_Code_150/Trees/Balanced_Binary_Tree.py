'''
USE DFS RECURIOSN 

Height Balalnced: A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.


Define another funtion to find height of tree -> same as maximum_depth_of_binary_tree,
Only difference in updating value of balanced inside the loop

#Update Balanced
#Saving in list to save to memory location otherwise can use 
# 'nonlocal diameter' or self.balanced 



--> Once balalnced becomes False, it should never be True again

--> Other method is kepeing track of both Bool and height in side the depth_dfs fucntion: [True, height]
----> In that case also do outptut[0] = ( (left[0] and right[0] and abs(left[1] - right[1])<=1)


'''

 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = [True]
        if root == None:
            return True

        def depth_dfs(node_):

            if node_ == None:
                return 0

            left = depth_dfs(node_.left)
            right = depth_dfs(node_.right)

            if abs(left - right)> 1:
                balanced[0] = False

            return max(left,right) + 1

        depth_dfs(root)
        return balanced[0]
        