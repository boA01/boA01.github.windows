from single_link_list import SingleLink

class Node():
    def __init__(self, data):
        self.data = data
        self.last = None
        self.next = None

class DoubleLink(SingleLink):
    def add(self, item):
        node = Node(item)
        if not self.is_empty(): # 不为空，就要当前驱
            self._head.last = node # 原首结点的前驱
        node.next = self._head # 后继为原首结点
        self._head = node # 头指向新节点
    
    def append(self, item):
        cur = self._head
        if not cur: # 空链表，则尾插法变首插法
            self.add(item)
            return
        while cur.next: # 找到尾结点————后继为空
            cur = cur.next
        cur.next = Node(item) # 添加新的尾结点
        cur.next.last = cur # 指定尾结点的前驱

    def insert(self, pos, item):
        len_ = self.lenth()
        if pos < 0 or pos > len_:
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
            # 写法不一定
            cur.next.last = node
            node.next = cur.next
            node.last = cur
            cur.next = node

    def remove(self, item):
        cur  = self._head
        if not cur: # 空链表，什么也不做
            return
        elif cur.data == item: # 删除首结点
            self._head = cur.next # 长度为一
            if cur.next: # 长度不为一（非尾结点）
                cur.next.last = None
            return
        while (p:=cur.next): 
            if p.data == item: # 定位目标结点
                cur.next = p.next # 尾结点
                if p.next:  # 非尾结点
                    p.next.last = cur
                return
            cur=cur.next

if __name__ == '__main__':
    dll = DoubleLink()
    print(dll.is_empty())
    print(dll.lenth())
    print(dll.search(5))

    dll.add(1)
    dll.remove(1)
    print("+++++++++++")
    dll.append(666)
    dll.append(999)
    dll.append(9)
    dll.add(1)
    dll.insert(0,0)
    dll.insert(5,5)

    print("+++++++++++")
    print(dll.lenth())
    dll.travel()
    dll.remove(999) #删除中间
    dll.remove(0) #删除首结点
    dll.remove(5) #删除尾结点
    dll.travel()
    print(dll.search(5))