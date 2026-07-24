class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n+1)
        g = [0] * (n+1)
        f[0] = g[0] = 1
        for i in range(1, n+1):
            f[i] = max(nums[i-1], g[i-1]*nums[i-1],f[i-1]*nums[i-1])
            g[i] = min(nums[i-1], g[i-1]*nums[i-1],f[i-1]*nums[i-1])
        return max(f[1:])
    
        """
        考虑到i元素是正还是负。然后前一个dp[i-1]需要的是最大还是最小值。
        建立两个dp表是如果不想考虑所有正负就直接把所有可能用max/min框起来
        """