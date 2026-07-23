# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(node, depth):
            if node == None:
                return depth
            d1, d2 = depth, depth
            if node.left != None:
                d1 = traverse(node.left, depth+1)
            if node.right != None:
                d2 = traverse(node.right, depth+1)

            return max(depth, d1, d2)
        
        if (root == None):
            return 0
        return traverse(root,1)