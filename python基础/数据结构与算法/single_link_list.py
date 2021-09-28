# 结点
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 链表
class SingleLink():
    def __init__(self, node=None):
        self._head = node

    '''
    判空
    '''
    def is_empty(self):
        return self._head==None

    '''
    长度
    '''
    def lenth(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    '''
    遍历
    '''
    def travel(self):
        cur = self._head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    '''
    头插法
    '''
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
    
    '''
    尾插法
    '''
    def append(self, item):
        cur = self._head
        if cur == None:
            self._head = Node(item)
            return
        while cur.next:
            cur = cur.next
        cur.next = Node(item)
    
    '''
    直插法
    '''
    def insert(self, pos, item):
        if pos > self.lenth() or pos < 0:
            print("下标错误")
        elif pos == 0:
            self.add(item)
        else:
            cur = self._head
            for i in range(pos-1):
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node

    '''
    移除
    '''
    def remove(self, item):
        cur = self._head
        if cur == None:
            return
        elif cur.data == item:
            self._head = cur.next
            return
        while cur.next:
            if cur.next.data == item:
                cur.next = cur.next.next
                return
            cur = cur.next

    '''
    是否存在
    '''
    def search(self, item):
        cur = self._head
        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLink()
    print(ll.is_empty())
    print(ll.lenth())

    ll.append(666)
    ll.append(999)
    ll.append(9)
    ll.add(1)
    ll.insert(0,0)
    ll.insert(5,5)

    print("+++++++++++")
    print(ll.lenth())
    ll.travel()
    ll.remove(5)
    ll.travel()
    print(ll.search(9))
