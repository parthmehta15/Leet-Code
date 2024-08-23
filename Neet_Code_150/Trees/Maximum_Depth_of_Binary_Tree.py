
'''
According to Leetcode:
Speed:
Ite. BFS > Rec. DFS > Ite. DFS

'''


''' 
Iterative BFS -> queue nested loop where remove all elements from queue and add 1 to depth
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        queue = []
        queue.append(root)
        depth = 0
        while queue:
            a =len(queue)
            for i in range(a):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth 



'''
Iterative DFS -> stack save node and depth in the stack

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        stack = []
        max_depth = 1  #Because there is atleast root node
        stack.append((root, 1))

        while stack:
            node, depth = stack.pop(-1)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))

            max_depth = max(max_depth, depth)

        return max_depth




'''

Using recursion - Recursive DFS

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1

        
        
        return max(depth_left, depth_right)
        