# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        self.dfs(root, 0, res)
        return sum(res)

    def dfs(self, root, cur, res):
        if not root:
            return
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            res.append(cur)
            return
        self.dfs(root.left, cur, res)
        self.dfs(root.right, cur, res)
