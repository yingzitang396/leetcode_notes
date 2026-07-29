# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        queue = deque([(root, 1)])
        while queue:
            level_q = len(queue)
            _, first_index = queue[0]
            for _ in range(level_q):
                node, index = queue.popleft()
                last_index = index
                if node.left:
                    queue.append([node.left, index * 2])
                if node.right:
                    queue.append([node.right, (index * 2) + 1])
            max_width = max(max_width, last_index - first_index +1)
        return max_width

        """
        tuple的话放进queue里面要注意queue也是要先拆list在倒进容器里所以 queue = deque([(root, 1)])
        _, first_index = queue[0]因为第一个node不需要用到只用下标为了节省空间可以不用，其实也是告诉大家这里不需要用到
         max_width = 0这个是为了最后max_width不会无脑被覆盖永远只返回最大值
        """
