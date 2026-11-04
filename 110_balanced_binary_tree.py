# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.dfs(root) == -1:
            return False
        return True

    def dfs(self, root) -> int:  # -1 means not balanced, 0,1,2,3,...means balanced (the height)
        if root is None:
            return 0
        l = self.dfs(root.left)
        if l == -1:
            return -1
        r = self.dfs(root.right)
        if r == -1:
            return -1
        if (abs(l - r) > 1):
            return -1
        return max(l, r) + 1
