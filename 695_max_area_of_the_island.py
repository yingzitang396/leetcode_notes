class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area_a = self.bfs(grid, visited, i, j, m, n)
                    max_area = max(max_area, area_a)
        return max_area

    def bfs(self, grid, visited, i, j, m, n):
        ret = 0
        queue = deque([(i,j)])
        visited[i][j] = True

        dx = (1, -1, 0, 0)
        dy = (0, 0, -1, 1)

        while queue:
            x, y = queue.popleft()
            ret += 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (0 <= nx < m and 0 <= ny < n
                        and grid[nx][ny] == 1
                        and not visited[nx][ny]):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        return ret

        

        """
        核心:if 后面的东西为 True,就进去执行
        if 就像一个门卫,它看后面那个表达式算出来是 True 还是 False:

        算出来 True → 开门,执行里面的代码
        算出来 False → 关门,跳过
        
        area_a = self.bfs(...) = 
        「叫我自己的 bfs 方法,从刚发现的这个岛的入口 (i,j) 出发,把整座岛数完,然后把面积还给我,存进 area_a」。

        「直接上」是因为:扫到新岛入口的这一刻,正是该启动 BFS 去数它的时候。
        主函数扫描 → 发现新岛 → 调 bfs 数面积 → 更新最大值
        """