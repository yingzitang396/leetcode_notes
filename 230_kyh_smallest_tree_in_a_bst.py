# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.temp = []
        self.dfs(root)
        return self.temp[k-1]

    def dfs(self, root):
        if root is None:
            return 
        self.dfs(root.left)
        self.temp.append(root.val)
        self.dfs(root.right)
 
 
 class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.dfs(root)
        return self.res

    def dfs(self, root) -> bool:      # 返回：这棵子树里找到答案了吗
        if root is None:
            return False              # 空树，没找到

        # ① 先搜左子树，如果左边就找到了，直接上报，不用管自己和右边
        if self.dfs(root.left):  # ← 改这里：加 if 接住左子树结果
            return True

        # ② 轮到自己，数一个
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return True               # 自己就是答案，上报

        # ③ 左边和自己都没找到，去右子树找，把右边的结果直接返回
        return self.dfs(root.right)       