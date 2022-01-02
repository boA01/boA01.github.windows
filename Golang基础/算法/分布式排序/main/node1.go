package main

import (
	"fmt"
	"net"
	"sort"

	"dc/pipelineMiddleWare"
)

func ServerMsgHandler(conn net.Conn, arr []int) {
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

func MsgHandler(conn net.Conn) {
	var arr []int
	buf := make([]byte, 16)
	// beatChan := make(chan struct{})
	// defer close(beatChan)

	// go HeartBeat(conn, beatChan, 30)

	clientip := conn.RemoteAddr()
	fmt.Println(clientip, "上线")

	for {
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		if n == 16 {
			n1 := pipelineMiddleWare.ByteToInt(buf[:8])
			n2 := pipelineMiddleWare.ByteToInt(buf[8:])
			// beatChan <- struct{}{}

			if n1 == 0 && n2 == 0 {
				arr = make([]int, 0, 10)
			} else if n1 == 1 {
				arr = append(arr, n2)
			} else {
				fmt.Println("接收完成", arr)
				sort.Ints(arr)
				fmt.Println("排序完成", arr)
				ServerMsgHandler(conn, arr)
				return
			}
		}
	}
}

func main() {
	serverListener, err := net.Listen("tcp", "0.0.0.0:9901")
	if err != nil {
		panic(err)
	}
	defer serverListener.Close()

	fmt.Println("已开启...")

	for {
		newConn, err := serverListener.Accept()
		if err != nil {
			panic(err)
		}
		go MsgHandler(newConn)
	}
}
