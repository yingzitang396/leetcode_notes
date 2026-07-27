# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lis = []
        queue = deque([root])
        flag = False
        while queue:
            level_q = len(queue)
            level = []
            for _ in range(level_q):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                level.append(node.val)
            if flag:
                level = level[::-1]
            lis.append(level)
            flag = not flag
        return lis

        """
        if flag:  # flag 为真时执行
        if not flag:  # flag 为假时执行(not 取反)
        
        为什么不用写 if flag == True:
        你之前写的是 if flag == True:,这也对,但多此一举。想一下:
        flag == True 是在问"flag 等于 True 吗?",结果本身又是一个 True 或 False。
        但 flag 本来就是 True 或 False 了,再拿它去和 True 比一次,绕了一圈,结果和直接用 flag 一模一样:
        flag == True    # flag 是 True → 结果 True;flag 是 False → 结果 False
        flag            # flag 是 True → 就是 True;flag 是 False → 就是 False
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if node.left: 的意思是"如果 node.left 存在(不是 None)"。
        因为 None 被当作"假",存在的节点被当作"真",所以效果和 != None 一样,但更简洁
        """
        
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        ret = []                          # List<List<Integer>> ret
        if not root:                      # if(root == null) return ret;
            return ret
        q = deque()                       # Queue<TreeNode> q = new LinkedList<>();
        q.append(root)                    # q.add(root);
        level = 1                         # int level = 1;

        while q:                          # while(!q.isEmpty())
            sz = len(q)                   # int sz = q.size();
            tmp = []                      # List<Integer> tmp = new ArrayList<>();
            for _ in range(sz):           # for(int i = 0; i < sz; i++)
                t = q.popleft()           # TreeNode t = q.poll();
                tmp.append(t.val)         # tmp.add(t.val);
                if t.left:                # if(t.left != null) q.add(t.left);
                    q.append(t.left)
                if t.right:               # if(t.right != null) q.add(t.right);
                    q.append(t.right)
            # 判断是否逆序
            if level % 2 == 0:            # if(level % 2 == 0) Collections.reverse(tmp);
                tmp.reverse()
            ret.append(tmp)               # ret.add(tmp);
            level += 1                    # level++;
        return ret
    
        """
        level = 1              # 开局:准备处理第1层

        while q:
            ...处理一层...
            if level % 2 == 0: # 用层号判断这层要不要反转
                tmp.reverse()
            ret.append(tmp)
            level += 1         # 这层处理完,层号+1,进入下一层
        """