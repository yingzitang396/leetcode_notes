# =============================================================================
# 206. Reverse Linked List（反转链表）
#
# 题目：给定单链表的头节点 head，反转链表，返回反转后的头节点。
# 例子：[1,2,3,4,5] -> [5,4,3,2,1]
#       [1,2]       -> [2,1]
#       []          -> []
#
# 核心：把每个节点的箭头 .next 掉头，改成指向前面
#       原来：None   1 → 2 → 3 → None
#       目标：None ← 1 ← 2 ← 3
#
# 两种方法对比：
#   方法               时间    空间    特点
#   prev 写法          O(n)    O(1)    面试最常见，最短
#   dummy 头插法       O(n)    O(1)    每个节点插到 dummy 后面最前面
# =============================================================================


# LeetCode 上这段是注释（系统已定义好），本地运行需要自己写出来
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# =============================================================================
# 方法一：prev 写法（推荐）
# 三个指针：
#   prev：已经反转好的部分的头，一开始是 None（什么都没有）
#   cur ：当前要掉头的节点，一开始是 head
#   nxt ：临时记住 cur 后面的节点，防止断开后找不到
# 口诀：存、掉头、prev 走、cur 走
# =============================================================================
class Solution1:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None          # 不需要 dummy，prev 从 None 开始
        cur = head
        while cur:
            nxt = cur.next   # ① 存：先记住后面
            cur.next = prev  # ② 掉头：cur 指向前面
            prev = cur       # ③ prev 走：前进到 cur
            cur = nxt        # ④ cur 走：前进到刚才存的 nxt
        return prev          # 循环结束 cur 一定是 None，prev 才是新的头


# =============================================================================
# 方法二：dummy 头插法
# 思路：每遇到一个节点，就把它插到 dummy 后面的第一个位置。
#       先来的被后来的挤到后面，顺序就反过来了。
# dummy.next 始终是"已经反转好的部分的头"，作用和方法一的 prev 一样
# =============================================================================
class Solution2:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur = head
        while cur:
            nxt = cur.next          # ① 存：先记住后面
            cur.next = dummy.next   # ② cur 先抓住 dummy 后面原来的第一个节点
            dummy.next = cur        # ③ dummy 再改成指向 cur，cur 插到了最前面
            cur = nxt               # ④ cur 走
        return dummy.next           # 跳过 dummy，返回真正的头


# =============================================================================
# 知识点笔记
# =============================================================================

# -----------------------------------------------------------------------------
# 1. 为什么一定要先存 nxt？
#    链表只能往后走。一旦执行 cur.next = prev，cur 和后面的节点就断开了，
#    如果没提前用 nxt 记住，后面整条链就找不到了。
#    所以 ① 存 必须在 ② 掉头 之前。
#
# 2. prev 写法逐步图解：1 → 2 → 3
#
#    开始：
#        prev    cur
#        None     1 → 2 → 3 → None
#
#    第 1 轮：
#      ① nxt = cur.next          记住 2
#      ② cur.next = prev         1 指向 None（1 和 2 断开，但 nxt 记着 2）
#            None ← 1      2 → 3 → None
#      ③ prev = cur              prev 到 1
#      ④ cur = nxt               cur 到 2
#                    prev  cur
#            None ←  1     2 → 3 → None
#
#    第 2 轮：2 指向 1，prev 到 2，cur 到 3
#            None ← 1 ← 2      3 → None
#    第 3 轮：3 指向 2，prev 到 3，cur 到 None
#            None ← 1 ← 2 ← 3      cur = None，循环停止
#
#    每轮结束后：
#      轮次     已反转部分（从 prev 开始）   cur
#      开始     None                          1
#      第 1 轮  1 → None                      2
#      第 2 轮  2 → 1 → None                  3
#      第 3 轮  3 → 2 → 1 → None              None，停止
#
# 3. 为什么 prev 从 None 开始，不能是 dummy？
#    第一轮 cur.next = prev 让节点 1 指向 prev。
#    反转后 1 是新的尾巴，尾巴后面应该什么都没有，也就是 None。
#    如果 prev = dummy，1 会指向 dummy，结果多出一个 0：
#        ✗ 5 → 4 → 3 → 2 → 1 → 0(dummy)
#        ✓ 5 → 4 → 3 → 2 → 1 → None
#
# 4. 为什么 return prev，不是 return cur？
#    循环停止的条件就是 cur 变成 None，所以结束时 cur 一定是 None。
#    prev 停在原来的最后一个节点，它才是新的头。
#
# 5. 头插法图解：1 → 2 → 3
#        开始：   dummy → None
#        处理 1： dummy → 1 → None
#        处理 2： dummy → 2 → 1 → None
#        处理 3： dummy → 3 → 2 → 1 → None
#        return dummy.next -> 3 → 2 → 1
#
# 6. 头插法里 ② ③ 的顺序不能换
#    插入要做两件事：cur 接上后面的，dummy 接上 cur
#      先 ② cur.next = dummy.next   cur 先抓住原来的第一个节点
#      再 ③ dummy.next = cur        dummy 改成指向 cur
#    如果先做 ③，dummy.next 已经变成 cur，再做 ② 就是 cur.next = cur，
#    自己指向自己，原来那部分链就丢了
#
# 7. 两种写法其实是一回事：dummy.next 就相当于 prev
#      prev 写法                  dummy 写法
#      prev = None                dummy = ListNode(0)   （dummy.next 默认是 None）
#      cur.next = prev            cur.next = dummy.next
#      prev = cur                 dummy.next = cur
#      return prev                return dummy.next
#    把左边的 prev 全部换成 dummy.next，就是右边
#
# 8. 86 题用 dummy，206 的 prev 写法为什么不用？
#    86 是往后接新节点，需要一个真实的车厢来挂东西 -> dummy 是 ListNode
#    206 是把箭头往回指，第一个节点往回指的应该是"什么都没有" -> prev 是 None
#
# 9. 要不要考虑空链表？
#    要。206 的 Constraints 是节点数 [0, 5000]，从 0 开始就有空链表。
#    但两种写法都不用单独处理：
#      head = None -> cur = None -> 循环一次都不执行
#      方法一 return prev       -> None
#      方法二 return dummy.next -> None（dummy.next 一直是初始的 None）
#    刷题习惯：先看 Constraints，范围从 0 开始就要想到空输入
#
# 10. 返回 None 为什么显示 []？链表的输出是 list 吗？
#    不是。函数签名 -> ListNode | None，返回的是头节点（或 None）。
#    [5,4,3,2,1] 只是 LeetCode 为了给人看做的转换：
#      输入：LeetCode 把 [1,2,3,4,5] 转成链表，把头节点传给 head
#      你的代码：处理链表，返回新的头节点
#      输出：LeetCode 从返回的节点顺着 .next 走一遍，收集成 [5,4,3,2,1] 显示
#    所以：
#      - None 就是空链表，LeetCode 显示成 []
#      - 不能写 return []，那是 Python 列表，类型错了
#      - 输入的 head 也不是 list，只能用 head.val、head.next，不能 head[0]、len(head)
#    方括号只是显示格式：简单好读，而且所有语言通用。二叉树的 [3,9,20,null,...] 也一样
# -----------------------------------------------------------------------------

# 我犯过的错误：
#   - 只写 dummy.next = cur; cur = cur.next
#       -> 只是 dummy 的箭头一直换指向，每个节点自己的箭头一个都没改
#       -> 头插法少了 nxt = cur.next 和 cur.next = dummy.next 两行
#   - prev 写法里 prev = dummy -> 结果多一个 0，应该 prev = None
#   - prev 写法里 return cur   -> cur 一定是 None，应该 return prev
#   - 以为反转链表需要 dummy  -> prev 写法不需要


# =============================================================================
# 本地测试工具
# =============================================================================
def build(values: list[int]) -> ListNode | None:
    """Python 列表 -> 链表（模拟 LeetCode 处理输入）"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None, limit: int = 12) -> list[int]:
    """链表 -> Python 列表（模拟 LeetCode 显示输出，最多走 limit 步防止成环）"""
    result = []
    while head and len(result) < limit:
        result.append(head.val)
        head = head.next
    return result


def wrong_first_attempt(head):
    """我最早的写法：只换 dummy 的指向，没改节点的箭头"""
    dummy = ListNode(0)
    cur = head
    while cur:
        dummy.next = cur
        cur = cur.next
    return dummy.next


def wrong_prev_dummy(head):
    """错误：prev 从 dummy 开始"""
    dummy = ListNode(0)
    prev, cur = dummy, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def wrong_swap_order(head):
    """错误：头插法先 ③ 再 ②，自己指向自己"""
    dummy = ListNode(0)
    cur = head
    while cur:
        nxt = cur.next
        dummy.next = cur        # ③ 先做了
        cur.next = dummy.next   # ② 这时 dummy.next 已经是 cur -> cur.next = cur
        cur = nxt
    return dummy.next


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),   # 空链表
    ]
    for sol in [Solution1(), Solution2()]:
        for values, expected in tests:
            result = to_list(sol.reverseList(build(values)))
            status = "✓" if result == expected else "✗"
            print(f"{status} {type(sol).__name__}: {values} -> {result} (expected {expected})")

    print("\n--- 错误写法演示，输入 [1,2,3] ---")
    print("只写 dummy.next = cur:", to_list(wrong_first_attempt(build([1, 2, 3]))))
    print("prev = dummy:         ", to_list(wrong_prev_dummy(build([1, 2, 3]))))
    print("② ③ 顺序换了（自环）: ", to_list(wrong_swap_order(build([1, 2, 3]))))