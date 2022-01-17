package main

import (
	"log"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

const HelloServiceName = "pkg.HelloService"

type HelloServiceInterface interface {
	Hello(args string, reply *string) error
}

type HelloService struct{}

func (p *HelloService) Hello(args string, reply *string) error {
	*reply = "hello " + args
	return nil
}

func RegisterService(svc HelloServiceInterface) error {
	return rpc.RegisterName(HelloServiceName, svc)
}

func main() {
	RegisterService(new(HelloService))

	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal("listenTCP error:", err)
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Accept error:", err)
		}

		// go rpc.ServeConn(conn)
		go rpc.ServeCodec(jsonrpc.NewServerCodec(conn)) // 跨语言
	}
}
