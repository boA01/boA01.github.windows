class Node():
    def __init__(self, item):
        self.data = item
        self.lchild = None
        self.rchild = None

class Tree():
    def __init__(self):
        self.root = None
    
    def add(self, item):
        node = Node(item)
        if self.root is None: #空树，先添加根
            self.root = node
            return
        queue = [self.root] # 放根
        while queue:
            cur_node = queue.pop(0) # 取结点
            if cur_node.lchild is None:
                cur_node.lchild = node
                # print(cur_node.data, '<<', node.data)
                return
            else:
                queue.append(cur_node.lchild) # 存结点

            if cur_node.rchild is None:
                cur_node.rchild = node
                # print(cur_node.data, '>>', node.data)
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self): #队列思想
        '''广度优先：bfs'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.data, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    
    def depth_travel(self): #栈思想
        '''深度优先：dfs'''
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            cur_node = stack.pop()
            print(cur_node.data, end=' ')
            if cur_node.rchild:
                stack.append(cur_node.rchild)
            if cur_node.lchild:
                stack.append(cur_node.lchild)

    def preorder(self, node):
        '''先序遍历'''
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        '''中序遍历'''
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.data, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        '''后序遍历'''
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.data, end=' ')

if __name__ == '__main__':
    tree = Tree()
    for i in [1, 2, 0, 3, 4]:
        tree.add(i)
    s = '''
     1
  2     0
3   4'''
    print(s)

    tree.breadth_travel()
    print()
    tree.depth_travel()
    print()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
