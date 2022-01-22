package main

import (
	"fmt"
	"log"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

func main() {
	conn, err := net.Dial("tcp", ":1234")
	if err != nil {
		log.Fatal("net.dial:", err)
	}

	client := rpc.NewClientWithCodec(jsonrpc.NewClientCodec(conn))

	var reply string
	err = client.Call("pkg.HelloService.Hello", "Haha", &reply)
	if err != nil {
		log.Fatal(err)
	}
	conn.Close()

	fmt.Println(reply)
}
