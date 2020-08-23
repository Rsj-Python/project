class Node():
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None
class SingleCycleLinkList():
    '''单向循环链表'''
    def __init__(self,node=None):
        self._head = node
        if node:
            node.next = node
    def is_empty(self):
        '''链表是否为空'''
        return self._head is None
    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        cursor = self._head #cursor指针，用来移动遍历节点
        count = 1 #count记录数量
        while cursor.next != self._head:
            count += 1
            cursor = cursor.next
        return count
    def travel(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        cursor = self._head
        while cursor.next != self._head:
            print(cursor.elem,end=' ')
            cursor = cursor.next
        # 退出循环,cursor指向尾节点，但尾节点的元素未打印
        print(cursor.elem,end='')
    def add(self,item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cursor = self._head
            while cursor.next != self._head:
                cursor = cursor.next
            # 退出循环,cursor指向尾节点
            node.next = self._head
            self._head = node
            cursor.next = node
    def append(self,item):
        '''链表尾部添加元素，尾插法'''
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cursor = self._head
            while cursor.next != self._head:
                cursor = cursor.next
            # 退出循环,cursor指向尾节点
            cursor.next = node
            node.next = self._head
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
        if self.is_empty():
            return -1
        pre = None
        cursor = self._head
        new_cursor = self._head
        while cursor.next != self._head:
            if cursor.elem == item:
                # 头结点的情况
                # 找尾节点
                if pre == None:
                    while new_cursor.next != self._head:
                        new_cursor = new_cursor.next
                    self._head = cursor.next
                    new_cursor.next = self._head
                else:
                    # 中间节点
                    pre.next = cursor.next
                return
            else:
                pre = cursor
                cursor = cursor.next
        # 退出循环,cursor 指向尾节点
        if cursor.elem == item:
            if pre == None:
                self._head = None
            else:
                pre.next = cursor.next
    def search(self,item):
        '''查找节点是否存在'''
        cursor = self._head
        while cursor.next != self._head:
            if cursor.elem == item:
                return True
            else:
                cursor = cursor.next
        if cursor.elem == item:
            return True
        return False
if __name__ == '__main__':
    mysll = SingleCycleLinkList()
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
    mysll.insert(-1,9) #9,8,1,2,3,4,5
    mysll.travel()
    print()
    mysll.insert(2,10)
    mysll.insert(8,34)
    mysll.travel()
    print()
    # print(mysll.length())
    mysll.remove(9)
    mysll.remove(34)
    mysll.remove(10)
    mysll.travel()
