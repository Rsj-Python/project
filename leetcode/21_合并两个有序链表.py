class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution():
    def mergeTwolists(self,l1,l2):
        head = ListNode(0)
        cur = head
        cur1 = l1
        cur2 = l2
        while cur1 and cur2 :
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        return head.next




# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 0-->1-->1-->2-->3-->4
#                     cur