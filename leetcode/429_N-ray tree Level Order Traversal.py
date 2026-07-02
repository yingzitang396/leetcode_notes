from typing import List, Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        s_list = []
        queue = deque()
        queue.append(root)
        while queue:
            level = len(queue)
            a_list = []
            for _ in range(level):
                temp = queue.popleft()
                a_list.append(temp.val)
                if temp.children:
                    queue.extend(temp.children)
            s_list.append(a_list)
        return s_list

        """
        if root is None:
            return []  在讨论edge case
        queue = deque([root])   # root是None，所以queue = deque([None]). Nonetype object
        queue.append(root)
        while len(queue) > 0:
            temp = queue.popleft()   # temp 现在是 None
            a_list.append(temp.val)  # ❌ 报错！None没有.val这个属性
        """
      
        """
        记住一个原则：
        return 一旦执行,函数立刻结束,所以只有当你确定"所有该做的事都做完了"才应该写 return。
        这道题里,只有 while 循环整个跑完（队列空了,说明所有层都处理完了）,才是真正该 return s_list 的时机。
        """

        """
        关于你问的 if temp.children: 是什么意思
        这是在判断 temp.children 是不是"真值"（truthy）。
        if temp.children:          # 翻译成人话：如果 temp.children 不是 None，也不是空列表
            queue.extend(temp.children)   # 才把孩子们加进队列
        """