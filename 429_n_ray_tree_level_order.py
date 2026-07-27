"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        lis = []
        queue = deque([root])
        # queue = deque()
        # queue.append(root)
        while queue:
            level_q = len(queue)
            level = []
            for _ in range(level_q):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            lis.append(level)
        return lis

        """
        
        not root 的意思是"root 是空的(None)时成立"。这是判断空树的标准写法。
        (也可以写 if root is None:,效果一样。但不要写 if root == []:,因为 root 是节点对象或 None,永远不会等于 []。)
        
        这里 self.children 存的就是"这个节点的所有孩子"。
        既然一个节点可能有好几个孩子(N叉树嘛),
        就得用一个能装多个东西的容器来存——也就是
        
        if node.children:              # 如果这个节点有孩子
            queue.extend(node.children)  # 就把所有孩子逐个加进队列
        
        if node.children: —— 判断这个容器空不空(有没有孩子)
        node.children 这个列表容器里,装的不是数字,而是一个个 Node 节点对象。
        所以你从里面拿出来的 child,本身也是个完整的节点,它自己也有 .val 和 .children。
        这就是为什么能一层层往下遍历——每个孩子又能找到它自己的孩子。
        
        再讲第一行:if node.children:

        这个 if 是保护措施,防止 children 是 None 时出错。

        回忆一下:叶子节点(没孩子的节点)的 node.children 可能是 None。
        如果直接 queue.extend(None),extend 想去"拆开 None",但 None 拆不开 → 报错。

        所以先用 if 挡一道:

        if node.children: 的意思是"如果 children 里有东西(非空、非None),才执行下面的 extend"。

        children 是 [5, 6](有内容)→ if 成立 → 执行 extend,加进去
        children 是 None 或 [](空的)→ if 不成立 → 跳过 extend,什么都不做

        这样 None 的情况就被 if 拦在门外,extend 只会在"确实有孩子"时才执行,永远不会碰到 None。

        queue.extend(node.children) —— 把这个容器拆开,里面的孩子逐个加进队列

        for child in node.children: —— 遍历这个容器,一个个把孩子拿出来
        for child in (node.children or []):
            if child.val > 0:        # 假设只想加某些孩子
                queue.append(child)

        这三种操作都是针对"列表容器"的常见操作,现在应该都串起来了
        
        这用到了 Python 里 or 的一个特性。先看 or 平时的样子:
        A or B,通常理解成"A 或 B 成立"。但 Python 的 or 实际上会返回一个具体的值,规则是:
        如果 A 是"有内容的/真的",就返回 A
        如果 A 是"空的/假的"(比如 None、[]、0),就返回 B
        """