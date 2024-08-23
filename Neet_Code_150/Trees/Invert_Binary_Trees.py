'''
Faster solution is with Recursion 
where you apply recursion on left side and then on right side

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

            if root == None:
                return 

            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)

            return root






'''
add root to queue
while loop while queue is not empty
add left and right to queue if exists
swap

take care of edge case is empty root

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return 
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left

        return root


        