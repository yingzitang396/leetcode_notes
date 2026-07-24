class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = [0] * (n+1)
        g = [0] * (n+1)
        for i in range(1, n+1):
            f[i] = max(nums[i-1], f[i-1] + nums[i-1])
            g[i] = min(nums[i-1], g[i-1] + nums[i-1])

        fmax = max(f[1:])
        gmin = min(g[1:])

        if fmax < 0:
            return fmax
        return max(fmax, total - gmin)

"""
考虑到连续数组中见的最大值，考虑到环形最大值是反向思考用中间连续数组的min求
f[1:]一次性取 f[1] 到 f[n] 的最大值，不会漏掉
fmax<0和 total = gmin是一样的，都是判断数组是不是全是负数，这样就不会取错。
if判断条件之后要return不然他仍然会执行下一个代码块

"""
