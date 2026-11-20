from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # 从0000开始用bfs思想往外找
        # 首先要想到极端情况 if0000是deadends直接返回-1
        # 遇到一个密码组合4位就要想到会有8种posiibility
        # 要创一个set去保存所有已经得到过的组合，一开始就要加入deadends
        # 因为这样一旦遇到的deadends的一致的组合就不会取关直接绕过
        # 新的尝试出的密码要去遍历这个set还有deadends
        # 一开始有dfs思想时候考虑每一轮是为一个step所以一开始就要设置steps=0
        # 要设立一个queue把每一层的密码放进去deque的时候去判断第几层
        # 如果目标组合已经在set就忽略，如果不在就加进add进set
        # 再去比较target是否在set
        # 全部循环结束发现没有就反-1

        # 从 0000 开始用 BFS 思想往外找
        # 1. 创建一个 set，一开始就把 deadends 加进去，遇到 deadend 就会直接绕过
        # 2. 极端情况：如果 0000 在 set 里（是 deadend），直接返回 -1
        # 3. 把 0000 放进 queue 和 set，设置 steps = 0
        # 4. queue 不空就循环，每一圈开始前用 len(q) 数一下这一圈有几个：
        #    - 从 queue 拿出一个密码 cur，如果 cur == target，返回 steps
        #    - 4 位密码有 8 种可能（4 个轮子 × 上下 2 个方向），用 % 10 处理 9→0、0→9
        #    - 新密码如果在 set 里就忽略；不在就加进 set，并放进 queue
        #    - 这一圈处理完，steps + 1
        # 5. 全部循环结束还没找到，返回 -1
        visited = set(deadends)
        if "0000" in visited:
            return -1
        step = 0
        queue = deque(["0000"])
        visited.add("0000")

        while queue:
            lq = len(queue)
            for _ in range(0, lq):
                password = queue.popleft()
                if password == target:
                    return step
                for i in range(4):
                    digit = int(password[i])
                    for nxd in [(digit - 1) % 10,  (digit + 1) % 10]:
                        nx = password[:i] + str(nxd) + password[i+1:]
                        if nx not in visited:
                            visited.add(nx)
                            queue.append(nx)
            step += 1
        return -1
