class Node():
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None
class SingleLinkList():
    '''单链表'''
    def __init__(self,node=None):
        self._head = node
    def is_empty(self):
        '''链表是否为空'''
        return self._head is None
    def length(self):
        '''链表长度'''
        cursor = self._head #cursor指针，用来移动遍历节点
        count = 0 #count记录数量
        while cursor != None:
            count += 1
            cursor = cursor.next
        return count
    def travel(self):
        '''遍历整个链表'''
        cursor = self._head
        while cursor != None:
            print(cursor.elem,end=' ')
            cursor = cursor.next
    def add(self,item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        node.next = self._head
        self._head = node
    def append(self,item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cursor = self._head
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = node
    def insert(self,pos,item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos < 1:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            node = Node(item)
            pre = self._head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node.next = pre.next
            pre.next = node
    def remove(self,item):
        '''删除节点'''
        pre = None
        cursor = self._head
        while cursor != None:
            if cursor.elem == item:
                # 先判断此节点是否是头结点
                # 头结点
                if pre == None:
                    self._head = cursor.next
                else:
                    pre.next = cursor.next
                break
            else:
                pre = cursor
                cursor = cursor.next
    def removeNthFromEnd(self,n):
        '''删除链表倒数第n个元素'''
        cursor = self._head
        count, res = 0, 0
        while cursor != None:
            cursor = cursor.next
            count += 1
        cursor = self._head
        while res != count - n:
            cursor = cursor.next
            res += 1
        cursor.val = cursor.next.val
        cursor.next = cursor.next.next
    def search(self,item):
        '''查找节点是否存在'''
        cursor = self._head
        while cursor != None:
            if cursor.elem == item:
                return True
            else:
                cursor = cursor.next
        return False
if __name__ == '__main__':
    mysll = SingleLinkList()
    print(mysll.is_empty())
    print(mysll.length())

    mysll.append(1)
    print(mysll.is_empty())
    print(mysll.length())

    mysll.append(2)
    mysll.add(8)
    mysll.append(3)
    mysll.append(4)
    mysll.append(5)
    head = Node(10)
    print(head.elem)
    # mysll.insert(-1,9) #9,8,1,2,3,4,5
    # mysll.travel()
    # print()
    # mysll.insert(2,10)
    # mysll.travel()
    # print()
    # mysll.insert(8,34)
    # mysll.remove(9)
    # mysll.remove(34)
    # mysll.remove(10)
    # mysll.travel()
