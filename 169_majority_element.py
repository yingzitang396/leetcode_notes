# =============================================================================
# 169. Majority Element（多数元素）
#
# 题目：给定长度为 n 的数组 nums，返回出现次数 大于 n // 2 的元素。
#       题目保证这个元素一定存在。
# 例子：[3,2,3] -> 3；[2,2,1,1,1,2,2] -> 2
#
# 三种方法对比：
#   方法             时间     空间    特点
#   字典计数         O(n)     O(n)    直观，可以提前 return
#   Counter          O(n)     O(n)    代码最短，但要数完整个列表
#   摩尔投票         O(n)     O(1)    最省空间，面试加分
#   ✗ nums.count()   O(n²)    O(1)    放循环里会超时，不要用
# =============================================================================

from collections import Counter, defaultdict


# =============================================================================
# 方法一：字典计数（哈希表）
# 思路：边遍历边用字典记录每个数出现的次数，超过 n // 2 就返回
# =============================================================================
class Solution1:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}  # key: 数字, value: 出现次数
        for num in nums:
            # 先算右边：查 num 现在几次（没有就算 0），加 1
            # 再存左边：存回字典（key 不存在就新建，存在就覆盖）
            count[num] = count.get(num, 0) + 1
            # if 必须缩进在 for 里面，每一轮都检查
            if count[num] > len(nums) // 2:
                return num  # 返回数字本身（key），不是次数 count[num]


# 方法一变体：defaultdict
class Solution1b:
    def majorityElement(self, nums: list[int]) -> int:
        count = defaultdict(int)  # 不存在的 key 自动初始化为 0
        for num in nums:
            count[num] += 1       # 所以可以直接 += 1，不会 KeyError
            if count[num] > len(nums) // 2:
                return num


# =============================================================================
# 方法二：Counter
# =============================================================================
class Solution2:
    def majorityElement(self, nums: list[int]) -> int:
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
        # Counter(nums)             -> Counter({2: 4, 1: 3})  字典
        # .most_common(1)           -> [(2, 4)]               列表，里面是 (元素, 次数) 元组
        # [0]                       -> (2, 4)                 取列表第 0 个
        # [0]                       -> 2                      取元组第 0 个


# =============================================================================
# 方法三：摩尔投票法（Boyer-Moore Voting）
# 思路：众数和非众数两两抵消，众数次数 > n/2，最后剩下的一定是众数
#   key：当前候选的众数
#   freq：候选数抵消后剩下的票数
# 前提：题目保证众数存在；否则最后要再遍历一遍验证
# =============================================================================
class Solution3:
    def majorityElement(self, nums: list[int]) -> int:
        key = nums[0]
        freq = 1
        for i in range(1, len(nums)):  # i 是下标，用 nums[i] 取数字
            if freq == 0:              # 情况 A：票数归零，换候选人
                key = nums[i]
                freq = 1
            elif key == nums[i]:       # 情况 B：和候选人相同，+1
                freq += 1
            else:                      # 情况 C：不同，抵消 -1
                freq -= 1
        return key


# =============================================================================
# 知识点笔记
# =============================================================================

# -----------------------------------------------------------------------------
# 1. 字典基础：key -> value
#    count = {3: 2, 2: 1}  表示 3 出现 2 次，2 出现 1 次
#    count[3] = 2      存
#    count[3]          取（key 不存在会报 KeyError）
#    3 in count        判断 key 是否存在
#    len(count)        key 的个数
#
# 2. 变量名
#    count / counts / freq 都是自己起的名字，前后必须一字不差
#    Python 区分大小写：count、counts、Counts 是三个不同的变量
#    Counter（大写 C）是 collections 里的工具，名字固定
#    nums.count(x) 是列表的方法，字典没有 .count
#
# 3. 点 . 语法：东西.功能(参数)
#    count.get(num, 0)   用 count 这个字典的 get 功能
#    nums.append(5)      用 nums 这个列表的 append 功能
#    ✗ get(num, 0)        不知道查哪个字典
#    ✗ count(get(num, 0)) 把字典当函数调用了
#
# 4. count[num] = count.get(num, 0) + 1
#    赋值语句：先算右边，再存左边
#    count.get(num, 0)  -> 查 num 几次，查不到返回 0
#    + 1                -> get 执行完就是一个数字，可以直接加（和 len(nums) + 1 一样）
#    count[num] = ...   -> 存回去
#    等价写法：
#        old = count.get(num, 0)
#        count[num] = old + 1
#
# 5. key 自动登记
#    方括号赋值 count[num] = ... ：不存在就新建，存在就覆盖
#    方括号读取 count[num]       ：不存在就报 KeyError
#    所以右边读用 .get()，左边存用方括号
#
# 6. defaultdict 的副作用：只是读取不存在的 key，也会把它加进字典（值为 0）
#    判断 key 是否存在用 `in`，不会新增 key
#    Counter 读不存在的 key 返回 0，但不会新增，比 defaultdict 安全
#
# 7. for num in nums           -> num 是数字本身
#    for i in range(len(nums)) -> i 是下标，用 nums[i] 取数字
#    下标变量建议叫 i，不要叫 num
#
# 8. 缩进决定"谁属于谁"
#    缩进在 for 下面 -> 每一轮都执行
#    和 for 对齐     -> 循环结束后只执行一次
#    想每一轮都做的事就缩进到 for 里面
#
# 9. return num 还是 count[num]？
#    num 是"谁"（key），count[num] 是"多少"（value）
#    题目问哪个数字 -> return num
#
# 10. 三种括号
#    [ ] 列表 list    ( ) 元组 tuple    { } 字典 dict（有冒号）
#    [0] 是按位置取第 0 个元素，对列表和元组都适用
#
# 11. nums.count(num) 放循环里为什么超时？
#    每次调用都从头扫一遍，O(n)；放循环里 n × n = O(n²)
#    字典查 key 是 O(1)，总共 O(n)
#
# 12. 手写字典 vs Counter
#    手写版可以中途 return 提前结束；Counter 一定把整个列表数完
#    最坏情况（众数在后面）都要看完 n 个，所以复杂度都是 O(n)
#
# 13. if / elif / else
#    else: 里面再套 if  ==  elif
#    从上往下检查，碰到第一个成立的就执行，后面全部跳过，每轮只走一个分支
#
# 14. 三元表达式的坑
#    ✗ count += 1 if key == nums[i] else count - 1
#      解析成 count += (1 if ... else count - 1)，不是减 1
#    ✓ count += 1 if key == nums[i] else -1
# -----------------------------------------------------------------------------

# 我犯过的错误：
#   - 定义用 count，使用写成 counts / 定义用 freq，使用写成 count -> NameError
#   - counts(get(num, 0)) -> 应该是 count.get(num, 0)
#   - if 没缩进到 for 里面 -> 只检查最后一个数，可能返回 None
#   - return count[num] -> 返回了次数，应该 return num
#   - 三元表达式写成 else count - 1 -> 应该 else -1
#   - 代码顶格 -> IndentationError


# =============================================================================
# 演示：自己跑一下看结果
# =============================================================================
def demo_dict_registration():
    """看字典每一轮怎么变化"""
    print("--- 字典每轮变化 ---")
    count = {}
    for num in [3, 2, 3]:
        count[num] = count.get(num, 0) + 1
        print(num, count)


def demo_defaultdict_side_effect():
    """defaultdict 只读一下也会新增 key"""
    print("--- defaultdict 副作用 ---")
    count = defaultdict(int)
    for num in [3, 2, 3]:
        count[num] += 1
    print("循环后:", dict(count), "len =", len(count))
    _ = count[5]  # 只是读一下
    print("读 count[5] 后:", dict(count), "len =", len(count))


def demo_counter_chain():
    """Counter 链式调用一步步看"""
    print("--- Counter 拆解 ---")
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Counter(nums))
    print(Counter(nums).most_common(1))
    print(Counter(nums).most_common(1)[0])
    print(Counter(nums).most_common(1)[0][0])


if __name__ == "__main__":
    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1, 2, 2], 2),
        ([1, 1, 2, 2, 2], 2),
        ([5], 5),
    ]
    for sol in [Solution1(), Solution1b(), Solution2(), Solution3()]:
        for nums, expected in tests:
            result = sol.majorityElement(nums)
            status = "✓" if result == expected else "✗"
            print(f"{status} {type(sol).__name__}: {nums} -> {result} (expected {expected})")
    print()

    demo_dict_registration()
    demo_defaultdict_side_effect()
    demo_counter_chain()