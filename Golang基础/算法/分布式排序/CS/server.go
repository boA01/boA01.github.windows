package main

import (
	"fmt"
	"log"
	"net"
	"os/exec"
	"time"
)

// 心跳
func HeartBeat(conn net.Conn, heartChan chan byte, timout int) {
	for {
		select {
		case hc := <-heartChan:
			log.Println(string(hc))
			conn.SetDeadline(time.Now().Add(time.Duration(timout) * time.Second))
		case <-time.After(time.Second * 30):
			conn.Close()
			return
		}
	}
}

func MsgHandler(conn net.Conn) {
	buf := make([]byte, 1024)
	clientip := conn.RemoteAddr()
	beatChan := make(chan byte)
	defer close(beatChan)

	go HeartBeat(conn, beatChan, 30)

	for {
		n, err := conn.Read(buf)
		if err != nil {
			log.Println(clientip, "time out")
			return
		}

		msg := buf[0]
		beatChan <- msg

		// 自定义协议
		if n != 0 {
			s1 := string(msg)
			s2 := string(buf[1:n])
			str := string(buf[:n])
			if s1 == "0" {
				fmt.Println(clientip, " data:\n", s2)
			} else if s1 == "1" {
				exec.Command(s2).Run()
			} else {
				fmt.Println(clientip, "\n", str)
			}
			conn.Write([]byte("收到" + str))
		}
	}
}

func main() {
	serverListener, err := net.Listen("tcp", "0.0.0.0:8848")
	if err != nil {
		panic(err)
	}
	defer serverListener.Close()

	for {
		newConn, err := serverListener.Accept()
		if err != nil {
			panic(err)
		}
		go MsgHandler(newConn)
	}
}
