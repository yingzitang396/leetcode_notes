# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)

    def dfs(self, root):
        if root.val == 0 :
            return False
        if root.val == 1:
            return True
        lef = self.dfs(root.left)
        rig = self.dfs(root.right)
        if root.val == 2:
            return lef or rig
        if root.val == 3:
            return lef and rig
        
        
        
        
方法2:剪支
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)

    def dfs(self, root):
        if root.val == 0 :
            return False
        if root.val == 1:
            return True
        lef = self.dfs(root.left)
        if lef == True and root.val == 2:
            return True
        rig = self.dfs(root.right)
        if root.val == 2:
            return lef or rig
        if root.val == 3:
            return lef and rig