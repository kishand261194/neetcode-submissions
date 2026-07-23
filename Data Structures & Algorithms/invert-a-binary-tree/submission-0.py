# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(queue):
            if len(queue) == 0:
                return
            node = queue.popleft()

            if (node == None):
                return
            
            if (node.right != None):
                queue.append(node.right)
            if (node.left != None):
                queue.append(node.left)
            
            left = node.left
            node.left = node.right
            node.right = left
            traversal(queue)
        
        queue = deque([root])
        traversal(queue)
        
        return root