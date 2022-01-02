package main

import (
	"net/http"
	"net/rpc"
)

type Args struct {
	A, B int
}

type Last int

func (t *Last) Mutiply(args *Args, reply *int) error {
	*reply = args.A * args.B
	return nil
}

func main() {
	la := new(Last)
	rpc.Register(la) // 注册类型
	rpc.HandleHTTP() // 设定http类型

	err := http.ListenAndServe(":1234", nil)
	if err != nil {
		panic(err)
	}
}
