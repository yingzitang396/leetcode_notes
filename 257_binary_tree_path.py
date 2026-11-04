# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ret = []
        self.dfs(root, "")
        return self.ret
    
    def dfs(self, root, path):
        if root is None:
            return
        path += str(root.val) + "->"
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        if root.left is None and root.right is None:
            path = path[:-2]
            self.ret.append(path)