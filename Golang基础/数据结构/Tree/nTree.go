package Tree

import "fmt"

type Dept struct {
	id   int
	name string
	pid  int
}

type Node struct {
	Dept
	son map[int]*Node
}

var fk = []Dept{
	{id: 1, name: "部门1", pid: 0},
	{id: 2, name: "部门2", pid: 1},
	{id: 3, name: "部门3", pid: 1},
	{id: 4, name: "部门4", pid: 3},
	{id: 5, name: "部门5", pid: 4},
}

func InitDeptTree(dept Dept) *Node {
	return &Node{
		Dept: dept,
		son:  make(map[int]*Node),
	}
}

var cur_ = new(Node)

func (root *Node) FindNode(id int) *Node {
	if root.id == id {
		cur_ = root
	} else {
		for _, v := range root.son {
			if v.id == id {
				cur_ = v
			} else if len(v.son) != 0 {
				v.FindNode(id)
			}
		}
	}
	return cur_
}

func (root *Node) Add(dept Dept) {
	pNode := root.FindNode(dept.pid)
	pNode.son[dept.id] = InitDeptTree(dept)
}

func main() {
	// sort.Slice(fk, func(i, j int) bool { return fk[i].pid > fk[j].pid })
	// fmt.Println(fk)

	pTree := InitDeptTree(Dept{id: 1, name: "部门1", pid: 0})
	// fmt.Printf("%#v\n", pTree)
	// pTree.Add(Dept{id: 2, name: "部门2", pid: 1})
	// fmt.Printf("%#v\n", pTree.son[2])

	for _, v := range fk[1:] {
		pTree.Add(Dept(v))
	}
	fmt.Printf("%#v", pTree.FindNode(5))
}
