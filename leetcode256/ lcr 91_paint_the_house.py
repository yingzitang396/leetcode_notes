def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        f = [0] * n
        g = [0] * n
        z = [0] * n
        f[0] = costs[0][0]
        g[0] = costs[0][1]
        z[0] = costs[0][2]
        for i in range(1, n):
            f[i] = min(g[i-1], z[i-1]) + costs[i][0]
            g[i] = min(f[i-1], z[i-1]) + costs[i][1]
            z[i] = min(f[i-1], g[i-1]) + costs[i][2]
        return min(f[n-1], g[n-1], z[n-1])

# 建立三个dp表格去比较red， green， blue的最小值
# 确认i的状态，以i位置结尾，粉刷red，green， blue的总体cost最小

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n+1)]  # 创建二维数组
        for i in range(1, n+1):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][0]
            # 因为dp表加了虚拟节点0使得第一个格子可以进入for循环所以costs二维表里的i需要减少一位
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][2]
        return min(dp[n][0], dp[n][1], dp[n][2])

