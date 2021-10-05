from single_link_list import *

class SingleLoopLink(SingleLink):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = self._head

    def lenth(self):
        cur = self._head
        if cur == None:
            return 0
        count = 1
        while cur.next != self._head:
            count+=1
            cur = cur.next
        return count
    
    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.data, end=' ')
            cur = cur.next
        print(cur.data)

    def add(self, item):
        node = Node(item)
        cur = node.next = self._head # 后继为原首结点
        self._head = node # 头指向新节点
        
        if cur is None: # 空链表
            node.next = node # 后继指向自己
        else:
            while cur.next != self._head.next: # 寻找尾结点
                cur = cur.next
            cur.next = self._head # 尾结点后继指向新首结点

    def append(self, item):
        cur = self._head
        if cur is None: # 空链表，则尾插法变首插法
            self.add(item)
            return
        while cur.next != self._head: # 非空链表，找到尾结点
            cur = cur.next
        cur.next = Node(item) # 更新的尾结点
        cur.next.next = self._head # 尾结点后继指向首结点

    def insert(self, pos, item):
        len_ = self.lenth()
        if pos > len_ or pos < 0:
            print("下标错误")
        elif pos == 0: # 下标为0，头插法
            self.add(item)
        elif pos == len_: # 下标为长度，尾插法
            self.append(item)
        else:
            cur = self._head
            for i in range(pos-1): # 定位到指定下标结点的前驱
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        if not cur:
            return
        
        elif cur.data == item: # 删除首结点
            if cur.next == cur: # 长度为一
                self._head = None
                return

            while cur.next != self._head: # 长度不为一，先寻找尾结点
                cur = cur.next
            cur.next = self._head.next # 尾结点指向新首结点
            self._head = cur.next # 头指向新首结点
        
        else:
            while cur.next.data != item: # 寻找目标结点的前驱
                cur = cur.next
                
                if cur == self._head: # 不存在删除对象
                    return
            cur.next = cur.next.next # 架空目标结点
    
    def search(self, item):
        cur = self._head
        if not cur:
            return False

        if cur.data == item: # 是否为首结点
            return True

        while cur.next != self._head:
            if cur.data == item: # 是否为中间结点
                return True
            cur = cur.next

        if cur.data == item: # 是否为尾结点
            return True

        return False

if __name__ == '__main__':
    ll = SingleLoopLink()
    print(ll.is_empty())
    print(ll.lenth())
    print(ll.search(5))

    ll.add(1)
    ll.remove(1)
    print("+++++++++++")
    ll.append(666)
    ll.append(999)
    ll.append(9)
    ll.add(1)
    ll.insert(0,0)
    ll.insert(5,5)

    print("+++++++++++")
    print(ll.lenth())
    ll.travel()
    ll.remove(999) #删除中间
    ll.remove(0) #删除首结点
    ll.remove(5) #删除尾结点
    ll.travel()
    print(ll.search(5))