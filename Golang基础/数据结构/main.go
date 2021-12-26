package main

import (
	"fmt"

	ArrayList "ds/ArrayList"
	LinkList "ds/LinkList"
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

func main() {
	list := ArrayList.NewArray()
	link := LinkList.Init()

	testList(list)
	testLink(link)
}
