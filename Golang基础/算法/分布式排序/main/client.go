package main

import (
	"fmt"
	"net"
)

func main() {
	tcpAddr, err := net.ResolveTCPAddr("tcp4", "127.0.0.1:8848")
	if err != nil {
		panic(err)
	}

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		panic(err)
	}

	conn.Write([]byte("hello"))

	var inputStr string
	buf := make([]byte, 1024)

	for {
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		fmt.Println(string(buf[:n]))

		fmt.Scanln(&inputStr)
		conn.Write([]byte(inputStr))
	}
}
