class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 3 for _ in range(n)]
        g = [[0] * 3 for _ in range(n)]
        f[0][0] = -prices[0]
        f[0][1] = f[0][2] = float('-inf')
        g[0][1] = g[0][2] = float('-inf')
        for i in range(1, n):
            for j in range(3):
                f[i][j] = max(f[i-1][j], g[i-1][j] - prices[i])
                g[i][j] = g[i-1][j]
                if j-1 >= 0:
                    g[i][j] = max(g[i-1][j], f[i-1][j-1] + prices[i])
        ret = 0
        for i in range(3):
            ret = max(ret, g[n-1][i])
        return ret


        """注意创建负无穷大时float('inf')
        然后还有括号问题写的时候要注意
        最后注意结果如果被题目需要的话需要return，这个东西ai检查不出来
        """