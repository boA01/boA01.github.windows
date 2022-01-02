package main

import (
	"fmt"
	"net"
	"sort"

	"dc/pipelineMiddleWare"
)

func send(conn net.Conn, arr []int) {
	// 00 开始
	btsStart := pipelineMiddleWare.IntToByte(0)
	btsStart = append(btsStart, pipelineMiddleWare.IntToByte(0)...)
	conn.Write(btsStart)

	for _, v := range arr {
		btsData := pipelineMiddleWare.IntToByte(1)
		btsData = append(btsData, pipelineMiddleWare.IntToByte(v)...)
		conn.Write(btsData)
	}

	// 01 结束
	btsEnd := pipelineMiddleWare.IntToByte(0)
	btsEnd = append(btsEnd, pipelineMiddleWare.IntToByte(1)...)
	conn.Write(btsEnd)

	fmt.Println("发送完成")
}

func main() {
	tcpAddr, err := net.ResolveTCPAddr("tcp4", "127.0.0.1:8848")
	if err != nil {
		panic(err)
	}

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		panic(err)
	}

	buf := make([]byte, 16)
	var arr []int

	for {
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		// fmt.Println(string(buf[:n]))

		if n == 16 {
			n1 := pipelineMiddleWare.ByteToInt(buf[:8])
			n2 := pipelineMiddleWare.ByteToInt(buf[8:])

			if n1 == 0 && n2 == 0 {
				arr = make([]int, 0, 10)
			} else if n1 == 1 {
				arr = append(arr, n2)
			} else {
				fmt.Println("接收完成", arr)
				sort.Ints(arr)
				fmt.Println("排序完成", arr)
				send(conn, arr)
				return
			}
		}
	}
}
