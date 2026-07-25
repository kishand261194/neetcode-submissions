# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def traversal(node):
            if node == None:
                return 0
            
            left = traversal(node.left)
            right = traversal(node.right)

            if (abs(left - right) >= 2):
                self.isBalanced = False 

            return 1 + max(left, right)
        
        traversal(root)
        return self.isBalanced
        