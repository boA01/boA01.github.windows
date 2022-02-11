package Tree

import (
	"fmt"
	"math"
)

type BinaryTree struct {
	value  int
	lChild *BinaryTree
	rChild *BinaryTree
}

func NewBinaryTree() *BinaryTree {
	return new(BinaryTree)
}

func (root *BinaryTree) InitBinaryTree(item int) {
	root.value = item
}

func InitBinaryTree(item int) *BinaryTree {
	return &BinaryTree{value: item}
}

// avl树
func (root *BinaryTree) AddNode(item int) {
	node := &BinaryTree{value: item}
	var queue = []*BinaryTree{root} // 队列
	for len(queue) > 0 {
		cur := queue[0]
		queue = append(queue[:0], queue[1:]...)
		if cur.lChild == nil {
			cur.lChild = node
			return
		} else {
			queue = append(queue, cur.lChild)
		}
		if cur.rChild == nil {
			cur.rChild = node
			return
		} else {
			queue = append(queue, cur.rChild)
		}
	}
}

// 广度优先
func (root *BinaryTree) Bfs() {
	var queue = make([]*BinaryTree, 0, 10) // 队列
	queue = append(queue, root)
	for len(queue) > 0 {
		cur := queue[0] // 首元素
		queue = append(queue[:0], queue[1:]...)
		fmt.Print(cur.value, "->")
		if cur.lChild != nil {
			queue = append(queue, cur.lChild)
		}
		if cur.rChild != nil {
			queue = append(queue, cur.rChild)
		}
	}
	fmt.Println()
}

// 深度优先
func (root *BinaryTree) Dfs() {
	var stack = make([]*BinaryTree, 0, 10) // 栈
	stack = append(stack, root)
	for len(stack) > 0 {
		end := len(stack) - 1
		cur := stack[end] // 尾元素
		stack = stack[:end]
		fmt.Print(cur.value, "->")
		if cur.rChild != nil {
			stack = append(stack, cur.rChild)
		}
		if cur.lChild != nil {
			stack = append(stack, cur.lChild)
		}
	}
	fmt.Println()
}

// 先序遍历
func Preorder(root *BinaryTree) {
	if root == nil {
		return
	}
	fmt.Printf("%d->", root.value)
	Preorder(root.lChild)
	Preorder(root.rChild)
}

// 中序遍历
func Inorder(root *BinaryTree) {
	if root == nil {
		return
	}
	Inorder(root.lChild)
	fmt.Printf("%d->", root.value)
	Inorder(root.rChild)
}

// 后序遍历
func Postorder(root *BinaryTree) {
	if root == nil {
		return
	}
	Postorder(root.lChild)
	Postorder(root.rChild)
	fmt.Printf("%d->", root.value)
}

// 结点数
func GetNodeNum(root *BinaryTree) int {
	if root == nil {
		return 0
	} else {
		return GetNodeNum(root.lChild) + GetNodeNum(root.rChild) + 1
	}
}

// 层数
func Layers(root *BinaryTree) int {
	if root == nil {
		return 0
	}
	leftLayers := Layers(root.lChild)
	rightLayers := Layers(root.rChild)
	if leftLayers > rightLayers {
		return leftLayers + 1
	} else {
		return rightLayers + 1
	}
}

// k层结点个数
func GetKthNum(root *BinaryTree, k int) int {
	if root == nil {
		return 0
	}
	if k == 1 {
		return 1
	}
	return GetKthNum(root.lChild, k-1) + GetKthNum(root.rChild, k-1)
}

// 叶子结点数目
func GetLeavNum(root *BinaryTree) int {
	if root == nil {
		return 0
	}
	if root.lChild == nil && root.rChild == nil {
		return 1
	}
	return GetLeavNum(root.lChild) + GetLeavNum(root.rChild)
}

// 是否平衡二叉树
func IsBalanced(root *BinaryTree) bool {
	if root == nil {
		return true
	}
	lde := Layers(root.lChild)
	rde := Layers(root.rChild)
	flag := false
	if (math.Abs(float64(lde - rde))) <= 1 {
		flag = true
	} else {
		flag = false
	}
	return flag && IsBalanced(root.lChild) && IsBalanced(root.rChild)
}
