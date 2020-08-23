class Stack():
    '''栈'''
    def __init__(self):
        self._list = []
    def push(self,item):
        '''添加一个新的元素到栈顶'''
        self._list.append(item)
    def pop(self):
        '''弹出栈顶元素'''
        print(self._list.pop())
    def peek(self):
        '''返回栈顶元素'''
        if self._list:
            return self._list[-1]
        else:
            return None
    def is_empty(self):
        '''判断栈是否为空'''
        return self._list == []
    def size(self):
        '''返回栈的元素个数'''
        return len(self._list)
if __name__ == '__main__':
    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.pop()
    print(mystack.is_empty())








