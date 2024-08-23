
'''
Recursion DFS
-> There are multiple base cases
1. If both empty return True
2. If above not executed and one of them is empty the return False
3. If both vales not equal return False

Next recursive call for left and right 

return left AND right

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        
        valid_left = self.isSameTree(p.left,q.left)
        valid_right = self.isSameTree(p.right,q.right)

        return valid_left and valid_right
        
        