class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, root, path):
        if root is None:
            return
        temp = path * 10 + root.val
        if root.left is None and root.right is None:
            self.sum += temp
            return
        self.dfs(root.left, temp)
        self.dfs(root.right, temp)