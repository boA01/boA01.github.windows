package LinkList

import (
	"fmt"
	_ "errors"
)

type LinkNode struct {
    data interface{}
    next *LinkNode
}

func Init() *LinkNode{
    head := new(LinkNode)
    return head
}

func (pl *LinkNode) Append(v interface{}) {
    cur := pl
    for ; cur.next != nil; cur = cur.next{}
    cur.next = &LinkNode{v, nil}
}

func (pl *LinkNode) Select() {
	cur := pl.next
	for {
		fmt.Println(cur.data)
        if cur.next == nil{
            break
        }
        cur = cur.next
    }
}