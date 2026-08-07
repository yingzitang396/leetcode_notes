class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)
        height = [[-1] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    visited[i][j] = True
                    queue.append((i, j))
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if (0 <= x < m and 0 <= y < n and isWater[x][y] == 0 and not visited[x][y]):
                    height[x][y] = height[a][b] + 1
                    visited[x][y] = True
                    queue.append((x,y))
        return height
