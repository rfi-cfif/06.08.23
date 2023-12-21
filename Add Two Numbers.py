class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Box:
    def __init__(self):
        self.head = None

    def add_head(self, head):
        self.head = head

def l_to_sl(l):
    val = l[0]
    next_node = ListNode(val)
    for val in l[1:]:
        node = ListNode(val, next_node)
        next_node = node
    # sl = Box()
    # sl.add_head(next_node)

    return next_node

def sl_to_num(sl):
    # node = sl.head
    node = sl
    num = ''
    while node is not None:
        num += str(node.val)
        node = node.next
    return int(num)

class Solution:
    def addTwoNumbers(self, l1, l2):
        sl1 = l_to_sl(l1)
        sl2 = l_to_sl(l2)
        num1 = sl_to_num(sl1)
        num2 = sl_to_num(sl2)
        return l_to_sl(list(str(num1 + num2))[::-1])

a = Solution()
res = a.addTwoNumbers([2,4,9], [5,6,4,9])
# res = a.addTwoNumbers([0], [0])
print(sl_to_num(res))
# l1 = [2,4,3], l2 = [5,6,4]
