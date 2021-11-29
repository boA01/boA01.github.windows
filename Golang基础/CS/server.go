package main

import (
    "fmt"
    _ "io"
    "net"
)

func process(conn net.Conn) {
    defer conn.Close()
    // 接收客户端发送的数据
    for {
        buf := make([]byte, 1024)
        n, err := conn.Read(buf)
        if err != nil {
            fmt.Println("客户端已下线")
            return
        }
        fmt.Printf("<<<%s", string(buf[:n]))
    }
}

func main() {
    fmt.Println("开始监听.....")

    // 开启监听
    listen, err := net.Listen("tcp", "0.0.0.0:8080")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(listen)

    for {
        // 建立连接
        conn, err := listen.Accept()
        if err != nil {
            fmt.Println(err)
        } else {
            fmt.Println("客户端：", conn.RemoteAddr().String())
            go process(conn)
        }
    }
}