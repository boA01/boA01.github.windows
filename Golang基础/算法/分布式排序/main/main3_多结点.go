package main

import (
	"fmt"
	"net"
	"strconv"
	"sync"

	"dc/pipelineMiddleWare"
)

var sortRes []<-chan int

func send(wg *sync.WaitGroup, conn net.Conn, arr []int) {
	defer wg.Done()

	clientip := conn.RemoteAddr()
	fmt.Println(clientip, "已连接")

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
	ServerMsgHandler(conn)
}

func ServerMsgHandler(conn net.Conn) {
	var arr []int
	buf := make([]byte, 16)
	var inCh = make(chan int, 1024)

	for {
		n, err := conn.Read(buf)
		if err != nil {
			return
		}
		if n == 16 {
			n1 := pipelineMiddleWare.ByteToInt(buf[:8])
			n2 := pipelineMiddleWare.ByteToInt(buf[8:])

			if n1 == 0 && n2 == 0 {
				arr = make([]int, 0, 10)
			} else if n1 == 1 {
				arr = append(arr, n2)
			} else {
				fmt.Println("接收完成", arr)
				for _, v := range arr {
					inCh <- v
				}
				close(inCh)
				sortRes = append(sortRes, inCh)
				return
			}
		}
	}
}

func main() {
	n := 2

	var wg sync.WaitGroup
	wg.Add(n)

	arrList := [][]int{{1, 4, 2, 5, 23}, {0, 4, 4, 546, 7, 34, 3}}

	for i := 0; i < n; i++ {
		fmt.Println("127.0.0.1:990" + strconv.Itoa(i))
		tcpAddr, err := net.ResolveTCPAddr("tcp4", "127.0.0.1:990"+strconv.Itoa(i+1))
		if err != nil {
			panic(err)
		}

		conn, err := net.DialTCP("tcp", nil, tcpAddr)
		if err != nil {
			panic(err)
		}

		go send(&wg, conn, arrList[i])
	}
	wg.Wait()

	last := pipelineMiddleWare.MergeN(sortRes...)
	for v := range last {
		fmt.Println(v)
	}
}
