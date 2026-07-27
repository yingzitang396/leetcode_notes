class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        s = " " + s
        for i in range(1, n+1):
            for j in range(i, 0, -1):
                if dp[j-1] and s[j: i+1] in words:
                    dp[i] = True
                    break
        return dp[n]            
        
        """判断是有最后一个单词分割进行状态判断
        s = " " + s这里虽然加了空格对齐了dp表格，但是dp状态仍然是原字符串是否包含在dictionary里面。
        """