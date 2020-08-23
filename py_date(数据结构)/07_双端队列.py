class Dqueue():
    '''双端队列'''

    def __init__(self):
        self._list = []

    def add_front(self, item):
        '''从头部添加一个item元素'''
        self._list.insert(0,item)

    def add_rear(self,item):
        '''从尾部添加一个元素'''
        self._list.append(item)

    def pop_front(self):
        '''从头部弹出元素'''
        return self._list.pop(0)
    def pop_rear(self):
        '''从尾部弹出元素'''
        return self._list.pop()
    def is_empty(self):
        return self._list == []
    def size(self):
        return len(self._list)

if __name__ == '__main__':
    mystack = Dqueue()
    mystack.add_front(1)
    mystack.add_front(2)
    mystack.add_rear(3)
    mystack.add_rear(4)
    print(mystack.pop_front())
    print(mystack.pop_front())
    print(mystack.pop_rear())
    print(mystack.pop_rear())