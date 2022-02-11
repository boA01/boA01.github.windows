package main

import (
	"fmt"

	// ArrayList "ds/ArrayList"
	// LinkList "ds/LinkList"
	Tree "ds/Tree"
)

type List interface {
	Size() int
	Get(index int) (interface{}, error)
	Set(index int, newVal interface{}) error
	Append(newVal interface{})
	Insert(index int, newVal interface{}) error
	Clear()
	Delete(index int) error
}

type Link interface {
	Append(interface{})
	Select()
}

func testList(l List) {
	l.Append(1)
	l.Append(2)
	l.Set(0, 999)
	l.Insert(0, 0)
	l.Append(3)
	l.Delete(1)
	l.Insert(1, 1)
	fmt.Println(l, l.Size())
}

func testLink(l Link) {
	l.Append(1)
	l.Append(2)
	l.Select()
}

func test2Tree() {
	// tree := NewBinaryTree()
	// tree.InitBinaryTree(0)
	tree := Tree.InitBinaryTree(10)

	for i := range [5]struct{}{} {
		tree.AddNode(i)
	}

	tree.Bfs()

	tree.Dfs()

	Tree.Preorder(tree)
	fmt.Println()

	Tree.Inorder(tree)
	fmt.Println()

	Tree.Postorder(tree)
	fmt.Println()

	fmt.Println("结点数目：", Tree.GetNodeNum(tree))
	fmt.Println("层数：", Tree.Layers(tree))
	fmt.Println("2层结点个数：", Tree.GetKthNum(tree, 2))
	fmt.Println("叶子结点数目：", Tree.GetLeavNum(tree))
	fmt.Println("是否平衡：", Tree.IsBalanced(tree))
}

func main() {
	// list := ArrayList.NewArray()
	// link := LinkList.Init()

	// testList(list)
	// testLink(link)

	test2Tree()
}
