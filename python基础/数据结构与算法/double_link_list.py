from single_link_list import SingleLink

class Node():
    def __init__(self, data, last=None, next=None):
        self.data = data
        self.last = last
        self.next = next

class DoubleLink(SingleLink):
    def add(self, item):
        node = Node(item)
        # 不为空，就要当前驱
        if not self.is_empty():
            self._head.last = node
        node.next = self._head
        self._head = node
        
    
    def append(self, item):
        cur = self._head
        # 空链表，则尾插法变首插法
        if not cur:
            self.add(item)
            return
        # 找到尾结点————后继为空
        while cur.next:
            cur = cur.next
        cur.next = Node(item)
        cur.next.last = cur

    def insert(self, pos, item):
        len_ = self.lenth()
        if pos < 0 or pos > len_:
            print("下标错误")
        elif pos == 0:
            self.add(item)
        elif pos == len_:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            # 定位到指定下标的前驱
            for i in range(pos-1):
                cur = cur.next
            # 写法不一定
            cur.next.last = node
            node.next = cur.next
            node.last = cur
            cur.next = node

    def remove(self, item):
        cur  = self._head
        # 空链表，什么也不做
        if not cur:
            return
        # 删除首结点
        elif cur.data == item:
            self._head = cur.next
            # 非尾结点
            if cur.next:
                cur.next.last = None
            return
        # 定位目标结点
        while (p:=cur.next):
            if p.data == item:
                cur.next = p.next
                # 非尾结点
                if p.next:
                    p.next.last = cur
                return
            cur=cur.next

if __name__ == '__main__':
    dll = DoubleLink()
    print(dll.is_empty())
    print(dll.lenth())

    dll.append(666)
    dll.append(999)
    dll.append(9)
    dll.add(1)
    dll.insert(0,0)
    dll.insert(5,6)

    print("+++++++++++")
    print(dll.lenth())
    dll.travel()
    dll.remove(0)
    dll.remove(999)
    dll.remove(6)
    dll.travel()
    print(dll.search(9))