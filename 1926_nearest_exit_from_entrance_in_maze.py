class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = [[False] * n for _ in range(m)]
        sr, sc = entrance[0], entrance[1]
        queue = deque ([(sr,sc)])
        visited[sr][sc] = True
        step = 0
        while queue:
            step += 1
            sz = len(queue)
            for i in range(sz):
                a, b = queue.popleft()
                for k in range(4):
                    x = a + dx[k]
                    y = b + dy[k]
                    if (0 <= x < m and 0 <= y < n and maze[x][y] == '.'
                            and not visited[x][y]):
                        if (x == 0 or y == 0 or x == m-1 or y == n-1):
                            return step
                        visited[x][y] = True
                        queue.append((x, y))
        return -1