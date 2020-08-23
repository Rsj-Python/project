class Node():
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.prev = None
class DoubleLinkList():
    '''双链表'''
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
        node.next.prev = node
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
            node.prev = cursor
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
            count = 0
            cursor = self._head
            while count < pos:
                count += 1
                cursor = cursor.next
            # 当循环退出后，pre指向pos-1位置
            node.next = cursor
            node.prev = cursor.prev
            cursor.prev.next = node
            cursor.prev = node
    def remove(self,item):
        '''删除节点'''
        cursor = self._head
        while cursor != None:
            if cursor.elem == item:
                # 先判断此节点是否是头结点
                # 头结点
                if cursor == self._head:
                    self._head = cursor.next
                    if cursor.next:
                        cursor.next.prev = None
                else:
                    cursor.prev.next = cursor.next
                    if cursor.next:
                        cursor.next.prev = cursor.prev
                break
            else:
                cursor = cursor.next
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
    mydou = DoubleLinkList()
    print(mydou.is_empty())
    print(mydou.length())

    mydou.append(1)
    print(mydou.is_empty())
    print(mydou.length())

    mydou.append(2)
    mydou.add(8)
    mydou.append(3)
    mydou.append(4)
    mydou.append(5)
    mydou.insert(-1, 9)  # 9,8,1,2,3,4,5
    mydou.travel()
    print()
    mydou.insert(2, 10)
    mydou.travel()
    print()
    mydou.insert(8, 34)
    mydou.travel()
    print()
    mydou.remove(9)
    mydou.remove(34)
    mydou.remove(10)
    mydou.travel()