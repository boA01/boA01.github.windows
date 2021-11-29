package main

import (
    "bufio"
    "fmt"
    "net"
    "os"
)

func main() {
    // 连接请求
    conn, err := net.Dial("tcp", "127.0.0.1:8080")

    if err != nil {
        fmt.Println(err)
    }
    fmt.Println(conn)

    for {
        reader := bufio.NewReader(os.Stdin)
        line, err := reader.ReadString('\n')

        if line == "exit\n" || err != nil {
            fmt.Println(err)
            break
        }

        _, err = conn.Write([]byte(line))
        if err != nil {
            fmt.Println(err)
        }
        // fmt.Printf("发送了%d字节\n", n)
    }
}