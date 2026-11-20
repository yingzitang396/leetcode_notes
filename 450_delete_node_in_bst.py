# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        #先找节点在删掉
        if root is None:
            return None
        parent, cur = None, root
        while cur:  # = while cur is not None:
            if key < cur.val:
                parent = cur
                cur = cur.left
            elif key > cur.val:
                parent = cur
                cur = cur.right
            else:
                if (cur.left is None and cur.right is None):
                    if cur is root:
                        return None
                    if parent.left is cur:
                        parent.left = None
                    else:
                        parent.right = None
                elif cur.left is None:
                    if cur is root:
                        return cur.right
                    if parent.left is cur:
                        parent.left = cur.right
                    else:
                        parent.right = cur.right
                elif cur.right is None:
                    if cur is root:
                        return cur.left
                    if parent.left is cur:
                        parent.left = cur.left
                    else:
                        parent.right = cur.left
                else:
                    rightminP = cur
                    rightmin = cur.right
                    while rightmin.left:
                        rightminP = rightmin
                        rightmin = rightmin.left
                    cur.val = rightmin.val
                    if rightminP.left is rightmin:
                        rightminP.left = rightmin.right
                    else:
                        rightminP.right = rightmin.right
                return root
        return root
