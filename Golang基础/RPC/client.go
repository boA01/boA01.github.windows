package main

import (
	"fmt"
	"net/rpc"
)

type Args struct {
	A, B int
}

func main() {
	server, err := rpc.DialHTTP("tcp", "127.0.0.1:1234")
	if err != nil {
		panic(err)
	}

	args := Args{2, 5}
	var reply int
	err = server.Call("Last.Multiply", args, &reply)
	if err != nil {
		panic(err)
	}
	fmt.Println(reply)
}
