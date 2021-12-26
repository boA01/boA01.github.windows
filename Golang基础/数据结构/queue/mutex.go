package mian

import (
	"fmt"
	"sync"
)

type Queue struct {
	queue []interface{}
	len   int
	lock  *sync.Mutex
}

func Init() *Queue {
	q := &Queue{}
	q.queue = make([]interface{}, 0)
	q.len = 0
	q.lock = &sync.Mutex{}
	return q
}

func main() {
	q := Init()

	fmt.Println("hello", q)
}
