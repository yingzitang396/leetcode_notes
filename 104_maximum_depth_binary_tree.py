# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self,root):
        if root == None:
            return 0
        lef = self.dfs(root.left)
        rig = self.dfs(root.right)
        return max(lef, rig) + 1


        