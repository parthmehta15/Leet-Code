# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # print(root)
        
        # is_sym = True
        queue = []
        
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False
        
        queue.append(root.left)
        queue.append(root.right)
        
        while len(queue)!= 0:
            # second_queue = []
            # print(queue)
            for i in range(int(len(queue)/2)):
                left_side = queue.pop(0)
                right_side = queue.pop(0)
                
                if left_side.val == right_side.val:
                    if left_side.left and right_side.right:
                        queue.append(left_side.left)
                        queue.append(right_side.right)
                        
                    elif left_side.left != right_side.right:
                        return False

                        
                if left_side.val == right_side.val:
                    if left_side.right and right_side.left:
                        queue.append(left_side.right)
                        queue.append(right_side.left)
                        
                    elif left_side.right != right_side.left:
                        return False
                        
                else:
                    return False
                        
        return True