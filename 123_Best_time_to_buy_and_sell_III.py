class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        k = min(k, n//2)
        f = [[float('-inf')] * (k + 1) for _ in range(n)]
        g = [[float('-inf')] * (k + 1) for _ in range(n)]
        f[0][0] = -prices[0]
        g[0][0] = 0
        for i in range(1, n):
            for j in range(k+1):
                f[i][j] = max(f[i-1][j], g[i-1][j] - prices[i])
                g[i][j] = g[i-1][j]
                if (j-1 >= 0):
                    g[i][j] = max(g[i-1][j], f[i-1][j-1] + prices[i])
        ret = 0
        for i in range(k+1):
            ret = max(ret, g[n-1][i])
        return ret
        

        """
        注意创建负无穷大时float('inf')
        然后还有括号问题写的时候要注意
        最后注意结果如果被题目需要的话需要return，这个东西ai检查不出来
        这里的k：
        k = min(k, n // 2) 确实是一个优化。原因是:一次完整的交易(买 + 卖)至少要占用两天(买一天、卖一天,且不能同一天),
        所以在 n 天里最多只可能完成 ⌊n/2⌋ 次交易。如果题目给的 k 特别大(比如 10^9),那多出来的交易次数是永远用不上的。
        把 k 截断到 n//2 之后:注意是整除，因为后面float'inf'必须是整数
        dp 表从 n × (k+1) 缩小成 n × (min(k, n//2)+1),空间变小;
        内层循环 for j in range(k+1) 的次数也变少,时间复杂度从 O(n·k) 降到 O(n · min(k, n//2)),
        最坏情况就是 O(n²),不会再被巨大的 k 拖垮。
        """