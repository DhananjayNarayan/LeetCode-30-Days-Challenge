# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current=root
        while current!=None:
            if current.val==val:
                return current
            if current.val>val:
                current=current.left
            else:
                current=current.right
        return current
        
