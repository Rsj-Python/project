
class ListNode():
    '''结点类'''
    def __init__(self,x):
        self.val = x
        self.next = None

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class Soultion():
    def addTwoNumbers(self,l1,l2):
        head = ListNode(0)
        node = head
        flag = 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum = num1 + num2 + flag
            flag = sum // 10
            node.next = ListNode(sum % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            node = node.next

        if flag != 0:
            node.next = ListNode(1)

        return head.next











