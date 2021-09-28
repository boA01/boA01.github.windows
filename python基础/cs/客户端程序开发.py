import socket as sk

if __name__ == "__main__":
    #1.创建tcp客户端套接字
    #AF_INET: ipv4地址类型
    #SOCK_STREAM：tcp传输协议类型
    tcp_client_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    ip = input("ip：")

    #2.和服务端套接字建立连接
    tcp_client_socket.connect((ip, 9090))

    
    #字符串转二进制
    send_data = input("发送：").encode("utf-8")

    #3.发送数据到服务端
    tcp_client_socket.send(send_data)

    #4.接收服务端数据
    #1024：每次接收数据最大字节数
    buffer=None
    while 1:
        d=tcp_client_socket.recv(1024)
        if d:
            buffer+=d
        else:
            break
    recv_data= b"".join(buffer)
    # 解码
    recv_content = recv_data.decode("utf-8")
    print("接收：", recv_content)

    #5.关闭套接字
    tcp_client_socket.close()
