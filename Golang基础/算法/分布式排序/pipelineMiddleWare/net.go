package pipelineMiddleWare

import (
	"bufio"
	"net"
)

func NetWordkWrite(addr string, in <-chan int) {
	listen, err := net.Listen("tcp", addr)
	if err != nil {
		panic(err)
	}

	go func() {
		defer listen.Close()

		conn, err := listen.Accept() //接收信息
		if err != nil {
			panic(err)
		}
		defer conn.Close()

		writer := bufio.NewWriter(conn)
		defer writer.Flush()
		WriterSlink(writer, in)
	}()
}

func NetWordkRead(addr string) <-chan int {
	out := make(chan int)

	go func() {
		conn, err := net.Dial("tcp", addr)
		if err != nil {
			panic(err)
		}

		r := ReadSource(bufio.NewReader(conn), -1)
		for v := range r {
			out <- v
		}
		close(out)
	}()
	return out
}
