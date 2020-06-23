# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        self.res = 0
        def count(node):
            if node is None:
                return
            self.res += 1
            count(node.left)
            count(node.right)
        
        count(root)
        return self.res
   
         
