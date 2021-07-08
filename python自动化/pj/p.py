import socket
import sys
import threading
import numpy as np
from PIL import Image

def main():
    #创建套接字
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #后去主机名称
    host = socket.gethostname()
    #设置端口
    port = 6666
    # 套接字与主机和端口号绑定
    serversocket.bind((host, port))
    # 设置监听最大连接数
    serversocket.listen(3)
    # 获取本地服务器连接信息
    myaddr = serversocket.getsockname()
    print(f"服务器地址：{str(myaddr)}")
    # 等待客户端信息
    while 1:
        # 获取客户端连接
        clientsocket, addr = serversocket.accept()
        print("连接地址：%s"%str(addr))
        try:
            # 为亲求开启线程
            t = ServerThreading(clientsocket)
            t.strat()
            pass
        except Exception as e:
            print(e)
            pass
        pass
    serversocket.close()
    pass

class ServerThreading(threading.Thread):
    def __init__(self, clientsocket, recvsize=1024**2, encoding="utf-8"):
        threading.Thread.__init__(self)
        self._socket = clientsocket
        self._recvsize = recvsize
        self._encoding = encoding
        pass

    def run(self):
        print("线程开启...")
        try:
            # 接收数据
            msg = ''
            while 1:
                # 读取recvsize个字节
                rec = self._socket.recv(self._recvsize)
                # 解码
                msg += rec.decode(self._encoding)
                # 文本是否接受完毕，
                # pyhton socket不能自己判断接收完毕，需要自定义标志数据结束接收
                if msg.strip().endswith('over'):
                    msg = msg[:-4]
                    break
            sendmsg = Image.open(msg)
            # 发送数据
            self._socket.send((f"{sendmsg}").encode(self._encoding))
            pass
        except Exception as e:
            self._socket.send("500".encode(self._encoding))
            print(e)
            pass
        finally:
            self._socket.close()
        print("任务结束！！！")
        pass

    def __del__(self):
        pass

if __name__ == "__main__":
    main()