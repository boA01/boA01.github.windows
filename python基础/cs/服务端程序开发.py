import socket as sk 
import threading as te

def client_request(new_client, ip_port):
    while True:
        print("客户端ip和端口：", ip_port)
        while True:
            #5.接收客户端数据
            recv_data = new_client.recv(1024)
            if recv_data:
                recv_content = recv_data.decode("utf-8")
                print("接收：", recv_content)

                #6.发送数据到客户端
                send_content = input("发送：")
                send_data = send_content.encode("utf-8")
                new_client.send(send_data)
            else:
                print(ip_port,"客户端已下线")
                break
        new_client.close()

if __name__ == "__main__":
    #1.创建tcp服务端套接字
    #AF_INET: ipv4地址类型
    #SOCK_STREAM：tcp传输协议类型
    tcp_server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    #设置端口号复用，程序退出端口号立即释放
    tcp_server_socket.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, True)
    
    #2.绑定端口号
    #ip不指定，表示主机上任意ip即可
    tcp_server_socket.bind(("", 9090))
    
    #3.设置监听
    #10：表示最大等待建立连接个数
    tcp_server_socket.listen(10)
    
    while True:
        #4.等待接收客户端请求
        new_client, ip_port = tcp_server_socket.accept()
        # print("客户端ip和端口：", ip_port)

        #创建子线程
        add_thread = te.Thread(target=client_request, args=(new_client, ip_port))
        #设置守护主线程
        add_thread.setDaemon(True)
        #启动子线程
        add_thread.start()
    
    #7.关闭套接字
    #服务器可以省略
    tcp_server_socket.close()