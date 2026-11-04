# =============================================================================
# 86. Partition List（分隔链表）
#
# 题目：给定链表头 head 和值 x，把所有 小于 x 的节点放在 大于等于 x 的节点前面，
#       两部分内部保持原来的相对顺序。
# 例子：[1,4,3,2,5,2], x=3 -> [1,2,2,4,3,5]
#       [2,1], x=2         -> [1,2]
#
# 思路：建两条链，遍历一次，
#       小于 x 的接到"小链"，大于等于 x 的接到"大链"，
#       最后把小链的尾巴接到大链的头。
#
# 时间：O(n)，只遍历一次
# 空间：O(1)，只多建了两个 dummy 节点，原节点重新连线，不新建节点
# =============================================================================


# LeetCode 上这段是注释（系统已定义好），本地运行需要自己写出来
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode(0)   # 小链的假头（值无所谓）
        dummy2 = ListNode(0)   # 大链的假头
        tail1 = dummy1         # 小链的最后一个节点，一开始就是 dummy1 本身
        tail2 = dummy2         # 大链的最后一个节点，一开始就是 dummy2 本身
        cur = head
        while cur:
            if cur.val < x:        # 比较的是节点的值 cur.val，不是节点 cur
                tail1.next = cur   # 第一步：连线，把 cur 接到 tail1 后面
                tail1 = tail1.next # 第二步：挪手指，tail1 移到 cur
            else:
                tail2.next = cur
                tail2 = tail2.next
            cur = cur.next         # 两个分支都要往后走，写在 if/else 外面
        tail2.next = None          # 断开大链尾巴，防止成环
        tail1.next = dummy2.next   # 小链尾巴接大链的头（跳过 dummy2）
        return dummy1.next         # 跳过 dummy1，返回真正的头


# =============================================================================
# 知识点笔记
# =============================================================================

# -----------------------------------------------------------------------------
# 1. ListNode() 是什么语法？
#    用类创建一个对象 = "按模板造一个新节点"
#    括号里的参数传给 __init__(self, val=0, next=None)
#        ListNode(5)   -> val=5, next=None
#        ListNode(0)   -> val=0, next=None
#        ListNode()    -> 没传参数，用默认值 val=0, next=None
#    和 dict()、Counter() 是同一个道理
#
# 2. 节点的基本操作
#        cur.val          读值
#        cur.next         下一个节点
#        cur.next = node  把 node 接在 cur 后面
#        cur = cur.next   cur 往后走一格
#
# 3. 遍历链表
#        cur = head
#        while cur:          # 等价于 while cur is not None
#            ...
#            cur = cur.next  # 忘了这句 -> 死循环
#
# 4. 为什么 dummy 是 ListNode(0)？0 是什么意思？
#    0 没有意义，写什么都行，ListNode() 也行
#    dummy 是占位用的假头：比较只看 cur.val，返回的是 dummy.next，
#    dummy 自己的值从来不会被用到
#        dummy1(0) -> 1 -> 2 -> 2
#          ↑          ↑
#         丢掉       return dummy1.next 从这里开始
#    好处：不用单独处理"头节点为空"的情况
#
# 5. dummy 不能是 None
#    dummy 必须是真的节点，后面才能往它的 .next 上接东西
#    dummy1 = None 的话，None 没有 .next -> AttributeError
#
# 6. 为什么 tail 从 dummy 本身开始，而不是 dummy.next？
#    区分两个东西：最后一个节点（盒子） vs 它后面的空位（None）
#
#         ┌─────────┐
#         │ val = 0 │
#         │ next ───┼──→ None
#         └─────────┘
#           dummy1
#
#    dummy1       是这个盒子本身，是真实的节点
#    dummy1.next  是盒子里的箭头，指向 None（后面什么都没有）
#
#    tail = "链的最后一个节点"。一开始链上只有 dummy，所以最后一个就是 dummy 本身
#        tail1 = dummy1        ✓ 指向盒子
#        tail1 = dummy1.next   ✗ 指向盒子后面的空气 None
#
#    为什么必须指向盒子：
#        tail1 = dummy1
#        tail1.next = cur      # tail1 就是 dummy1，所以等于 dummy1.next = cur
#    正因为 tail1 和 dummy1 是同一个节点，第一次接上时 dummy1 才真的连上了链，
#    最后 return dummy1.next 才能拿到结果
#
# 7. 为什么 None 不能接？
#    接新节点 = 修改某个盒子里的 next 箭头
#    None 不是盒子，没有 next 箭头 -> tail1.next = cur 会报 AttributeError
#
#    火车类比：
#      节点 = 车厢，.next = 车厢尾部的挂钩
#      dummy = 火车头，挂钩上暂时什么都没挂（next = None）
#      tail 要指向最后一节车厢，新车厢只能挂在车厢的挂钩上
#      不能挂在"最后一节车厢后面的空地"上，空地没有挂钩
#
# 8. tail 怎么往后移？先接上，再移动（两步都要做）
#        tail1.next = cur      # 连线：把 cur 接到 tail1 后面
#        tail1 = tail1.next    # 挪手指：tail1 移到 cur
#    ✗ 只写 tail1 = cur：只是变量换了指向，链表没连起来，dummy1.next 永远是 None
#    记法：.next = 是连线，tail = 是挪手指
#
# 9. cur.val vs cur
#    cur 是节点对象，不能直接和数字比
#        ✗ if cur < x:
#        ✓ if cur.val < x:
#
# 10. 为什么要 tail2.next = None？
#    大链最后一个节点的 next 还指着原链表里它后面的节点，不断开可能成环
#    例：[1,4,3,2,5,2], x=3
#        大链是 4 -> 3 -> 5，但 5 原来的 next 是最后那个 2
#        2 在小链里，小链尾巴又接回大链头 4 -> 无限循环
#        1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 2 -> 4 -> 3 -> 5 -> ...
#    （小链尾巴不用断，因为马上会被 tail1.next = dummy2.next 覆盖）
#
# 11. 最后两步
#        tail1.next = dummy2.next   # 接的是 dummy2.next（大链真正的头），不是 dummy2
#        return dummy1.next         # 返回 dummy1.next，不是 dummy1
#    这样写对空链表、全小于 x、全大于等于 x 都成立
# -----------------------------------------------------------------------------

# 我犯过的错误：
#   第一次：
#   - if cur.val < 3 -> 写死了 3，应该是 x
#   - tail1 = dummy1.next -> 应该是 tail1 = dummy1
#   - tail1 = cur 只挪手指没连线 -> 要先 tail1.next = cur 再 tail1 = tail1.next
#   - dummy2.next = cur -> 每次都覆盖 dummy2 后面那个，应该 tail2.next = cur
#   - cur = cur.next 只写在 else 里 -> 遇到小于 x 的节点 cur 不动，死循环
#   第二次：
#   - dummy1 = None -> 应该 dummy1 = ListNode(0)
#   - tail1 = dummy1.next -> 又写成了这个，应该 tail1 = dummy1
#   - if cur < x -> 应该 cur.val < x
#   - tail1 = cur -> 同第一次，没连线


# =============================================================================
# 本地测试工具
# =============================================================================
def build(values: list[int]) -> ListNode | None:
    """Python 列表 -> 链表"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)   # 同样的"先连线"
        tail = tail.next          # "再挪手指"
    return dummy.next


def to_list(head: ListNode | None, limit: int = 20) -> list[int]:
    """链表 -> Python 列表（最多走 limit 步，防止成环时死循环）"""
    result = []
    while head and len(result) < limit:
        result.append(head.val)
        head = head.next
    return result


def partition_without_cut(head: ListNode | None, x: int) -> ListNode | None:
    """演示：去掉 tail2.next = None 会怎样"""
    dummy1, dummy2 = ListNode(), ListNode()
    tail1, tail2 = dummy1, dummy2
    cur = head
    while cur:
        if cur.val < x:
            tail1.next = cur
            tail1 = tail1.next
        else:
            tail2.next = cur
            tail2 = tail2.next
        cur = cur.next
    # tail2.next = None   <- 故意不写
    tail1.next = dummy2.next
    return dummy1.next


if __name__ == "__main__":
    tests = [
        ([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),
        ([2, 1], 2, [1, 2]),
        ([], 1, []),                 # 空链表
        ([1, 2, 3], 5, [1, 2, 3]),   # 全小于 x
        ([5, 6, 7], 1, [5, 6, 7]),   # 全大于等于 x
    ]
    for values, x, expected in tests:
        result = to_list(Solution().partition(build(values), x))
        status = "✓" if result == expected else "✗"
        print(f"{status} {values}, x={x} -> {result} (expected {expected})")

    print("\n--- 不写 tail2.next = None（只打印前 20 个）---")
    print(to_list(partition_without_cut(build([1, 4, 3, 2, 5, 2]), 3)))