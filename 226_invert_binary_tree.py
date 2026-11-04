# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)

    def dfs(self, root):
        if root is None:
            return None
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        root.left = r
        root.right = l
        return root