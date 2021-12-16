
package tree

import (
    "math"
    "fmt"
)

type BinaryTree struct {
    Value int
    Left  *BinaryTree
    Right *BinaryTree
}

func InitBinaryTree(root *BinaryTree) *BinaryTree {
    l := BinaryTree{}
    r := BinaryTree{}
    root.Left = l.NewBinaryTreeNode(2)
    root.Right = r.NewBinaryTreeNode(3)
    l2:=BinaryTree{}
    ll2:=BinaryTree{}
    root.Left.Left = l2.NewBinaryTreeNode(4)
    root.Left.Right = ll2.NewBinaryTreeNode(5)
    return root
}

func (this *BinaryTree) NewBinaryTreeNode(value int) *BinaryTree {
    this.Value = value
    this.Left = nil
    this.Right = nil
    return this
}

// 计算二叉树节点个数
func GetNodeNum(root *BinaryTree) int {
    if root == nil {
        return 0
    } else {
        return GetNodeNum(root.Left) + GetNodeNum(root.Right) + 1
    }
}

// 计算二叉树的深度
func GetDegree(root *BinaryTree) int {
    if root == nil {
        return 0
    }
    var maxDegree = 0
    if GetDegree(root.Left) > GetDegree(root.Right) {
        maxDegree = GetDegree(root.Left)
    } else {
        maxDegree = GetDegree(root.Right)
    }
    return maxDegree + 1
}

// 前序遍历： 根-> 左子树 -> 右子树
func PreOrder(root *BinaryTree) {
    if root == nil {
        return
    }
    fmt.Printf("%d->", root.Value)
    PreOrder(root.Left)
    PreOrder(root.Right)
}

// 中序： 左子树-> 根 -> 右子树
func InOrder(root *BinaryTree) {
    if root == nil {
        return
    }
    InOrder(root.Left)
    fmt.Printf("%d->", root.Value)
    InOrder(root.Right)
}

// 后序： 左子树-> 右子树 ->  根
func PostOrder(root *BinaryTree) {
    if root == nil {
        return
    }
    PostOrder(root.Left)
    PostOrder(root.Right)
    fmt.Printf("%d->", root.Value)
}

//  求 K 层节点个数
func GetKthNum(root *BinaryTree ,k int ) int {
    if root==nil{
        return 0 
    }
    if k==1{
        return 1 
    }
    return GetKthNum(root.Left,k-1)+GetKthNum(root.Right,k-1)
}

// 求叶子节点个数
func GetLeavNum(root *BinaryTree) int {
    if root==nil{
        return 0
    }
    if root.Left==nil && root.Right == nil {
        return 1
    }
    return GetLeavNum(root.Left)+GetLeavNum(root.Right)
}


// 判断是否平衡二叉树
func IsBalanced(root *BinaryTree) bool {
    if root==nil{
        return  true
    }
    lde:=GetDegree(root.Left)
    rde:=GetDegree(root.Right)
    flag:=false
    if (math.Abs(float64(lde-rde)))<=1{
        flag=true
    }else{
        flag=false
    }
    return flag && IsBalanced(root.Left) && IsBalanced(root.Right)
}