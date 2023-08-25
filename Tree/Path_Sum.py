# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        queue = []
        total_sum = []
        
        leaf_nodes = []
        
        queue.append(root)
        total_sum.append(root.val)
        
        
        while len(queue) != 0:
            print(total_sum)
            # cache = total_sum[:]
            for i in range(len(queue)):
                curr_node = queue.pop(0)
                curr_sum = total_sum.pop(0)

                if curr_node.left:
                    total_sum.append(curr_sum + curr_node.left.val)
                    queue.append(curr_node.left)

                if curr_node.right:
                    total_sum.append(curr_sum + curr_node.right.val)
                    queue.append(curr_node.right)
                    
                if (not curr_node.left) and (not curr_node.right):
                    leaf_nodes.append(curr_sum)
                
        
        if targetSum in leaf_nodes:
            return True
        else:
            return False
            
                
                
        
        