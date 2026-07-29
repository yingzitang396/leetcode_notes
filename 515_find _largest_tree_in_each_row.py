# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_q = len(queue)
            max_value = float('-inf')
            for i in range(level_q):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                max_value = max(max_value, node.val)
            res.append(max_value)
        return res


        """注意maxvaluezailimianhaishizaiwaimian取决于是否每一行都需要更新最新的maxvalue
        """