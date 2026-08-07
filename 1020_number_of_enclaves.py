class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dx = (1, -1, 0, 0)
        dy = (0, 0, -1, 1)
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        # 从边界的1开始往里面走说明里面的1是可以walk off grid
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 1:
                    queue.append((i,j))
                    visited[i][j] = True

        # 所有的边界1作为一个起点：也就是多源往里面遍历四个方向，一边遍历一边加进queue 和visited里
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if (0 <= x < m and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]):
                    visited[x][y] = True
                    queue.append((x, y))
        
        # 返回结果不需要知道最短步数， 只需要返回不能走出去的1的个数
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    ret += 1
        return ret

