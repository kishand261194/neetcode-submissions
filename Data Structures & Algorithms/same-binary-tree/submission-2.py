# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.treea = [p]
        self.treeb = [q]

        def dfs(node, tree):
            if node == None:
                tree.append(node)
                return
            
            tree.append(node.left)
            dfs(node.left, tree)
            tree.append(node.right)
            dfs(node.right, tree)
        
        dfs(p, self.treea)
        dfs(q, self.treeb)

        if len(self.treea) != len(self.treeb):
            return False

        res = True
        for i in range(len(self.treea)):
            if (self.treea[i] == None and self.treeb[i] == None):
                continue

            if (self.treea[i] == None and self.treeb[i] != None):
                res = False
                break

            if (self.treea[i] != None and self.treeb[i] == None):
                res = False
                break

            if (self.treea[i].val != self.treeb[i].val):
                res = False
                break
        
        return res