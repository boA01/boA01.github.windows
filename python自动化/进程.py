'''
多任务
    IO密集型：python，操作IO
    计算密集型：c，提高cpu利用率，尽量少切换，任务数=核数

    同步：任务依次完成  子程序（函数<线程>）层级调用，通过栈实现，是线程切换
    异步：任务可以中断  协程调用，由子程序自己控制，不是线程切换

    并发：交替（任务（进程）数大于核数）；切换（保存现场，准备新环境等）是占用时间的
    并行：同时（多处理器或多核）<日常：听歌时聊天>

  多进程：听歌和聊天，稳定
  多线程：看电影（视频和音频两线程同时），内存消耗较少、要加锁
  多进程＋多线程，更充分也更复杂
  多进程+协程

  异步IO：单核-单进程，n核-n进程，充分利用IO

进程（任务）
资源分配的最小单位
可以分配到多cpu，多台机器（分布式）


线程（子任务）
执行的最小单位
共享全局变量（Lock）
只能分配到多个cpu

协程（微线程）
单线程的异步编程模型

前两是抢占式，后者是自己控制
'''

import os
import time
import random
import multiprocessing as mt #进程模块
import threading as td #线程模块
import subprocess #子进程模块
import asyncio

# 进程（资源分配的最小单位）

def fork_test():
    print(f"父进程{os.getpid()} start!!!")
    pid = os.fork() #Unix/Lixux，复制父进程，调用一次，返回两次（父子都返回）
    if pid == 0:
        print(f"子进程{os.getpid()} start!")
    else:
        print("!!!")
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def proc(name):
    print(f"chile process {name}({os.getpid()})")
    start_time = time.time()
    time.sleep(random.random()*2) #随机延迟
    end_time = time.time()
    print("%s runs %.2f" %(name,(end_time-start_time)))

def mt_test():
    #创建子进程
    p = mt.Process(target=proc,args=("test",))
    print("Child process will start")
    p.start() #进程开始
    p.join() #子进程等待，用于进程间同步
    print("Child process end")

    #进程池
    po = mt.Pool(3) #最多同时执行3个子进程，完成某一个后第四个才能开始
    for i in range(4):
        po.apply_async(proc,args=(i,)) #异步创建进程
    print("waiting fo all subprocess done...")
    po.close() #关闭进程池
    po.join() #等待所有子进程
    print("Done!")

# 子进程控制
def subpre_test():
    print("$ nslookup www.qq.com")
    r = subprocess.call(["nslookup","www.qq.com"])
    print(f"Exit code: {r}")

    po = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, err = po.communicate(input("<<<").encode("utf-8")) #继续输入
    print(output.decode("utf-8"))
    print(f"exit code: {po.returncode}")

# 进程间通信（管道<queue，pipe，fifo>，消息队列，信号，共享内存，套接字<网络，UNIX域>）

def p_w(q):
    for i in ["A","B","C"]:
        print(f"Process({os.getpid()}) to write：{i}")
        q.put(i) #
        time.sleep(random.random())
    pass

def p_r(q):
    while 1:
        print(f"Process({os.getpid()}) to read：{q.get()}")
    pass

# 分配到多核
def queue_test():
    q=mt.Queue()
    pw = mt.Process(target=p_w, args=(q,))
    pr = mt.Process(target=p_r, args=(q,))

    pw.start()
    pr.start()
    pw.join() #等待pr
    pr.terminate() #强行终止

# 分配到多主机（分布式进程）
'''

'''

# 线程（执行的最小单元）
# 理论上，n核cpu需要n个死循环线程才能跑满；
# python历史问题，解释器自带有GIL锁，不能多线程实现多核任务，利用率只能是100%
# 可以用多进程来实现多核任务
# cpu核数：mt.cpu_count()

def in_to():
    print(f"Thread({td.current_thread().name})")
    global p
    # 获取当前线程关联的m
    p+=local_x.m
    pass
    
def out_to():
    print(f"Thread({td.current_thread().name})")
    global p
    p-=local_x.m
    pass

def change_it(n):
    # 先存后取，结果应该为0:
    global p
    p+=n
    p-=n

# Lock（降低了效率）
def run_thread(n):
    global p
    # 绑定ThreadLocal的m
    local_x.m=n
    for i in range(2):
        #获取锁
        # lock.acquire()
        try:
            # in_to()
            # out_to()
            change_it(n)
        finally:
            #释放锁
            # lock.release()
            pass

def t2():
    print(p)
    c1 = td.Thread(target=run_thread,args=(2,))
    c2 = td.Thread(target=run_thread,args=(8,))

    c1.start()
    c2.start()
    c1.join()
    c2.join()
    print(p)

#协程
# 不是线程切换，由程序自身控制

# 消费者 一个generator
def consumer():
    r = ''
    while 1:
        n = yield r # 发送r的值（中断），赋值接收的n
        if not n: #没有生产
            return
        print(f"Consumer consuming {n}")
        r = "吃完了" 

# 生产者
def producer(c):
    c.send(None) # 启动生成器；等效：next(c)
    n = 0
    while n<5:
        n+=1
        print(f"Producer producing {n}")
        r = c.send(n) #发送n的值, 并next(c)，赋值接收的r
        print(f"Consumer return: {r}")
    c.close() # 不生产了，要关闭消费者
    print("歇业...")

def cp():
    c = consumer()
    print("开始")
    producer(c) #开始
    
'''
@asyncio.coroutine -> async
yield from -> await
'''

async def hello(s):
    print(f"hello {s}")
    # 异步调用asyncio.sleep(1)
    await asyncio.sleep(1)
    print("Hello again")

def hello_():
    # 获取EventLoop
    loop = asyncio.get_event_loop()

    tasks = [hello(i) for i in ['A','B','C']]

    # 执行coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()


#测试
def process_():
    print(f"parent process ({os.getpid()})")
    mt_test()
    # subpre_test()
    # queue_test()

def thread_():
    # current_thread()返回当前线程实例
    print(f"Thread({td.current_thread().name})")
    t2() #加锁；同一时刻，一个进程有锁

def gen_():
    # cp()
    hello_()


p=100
# lock = td.Lock() #创建锁
local_x = td.local() #创建全局ThreadLocal对象
# 常用在为每个线程绑定数据库连接，http请求等，方便处理函数访问这些资源

# def score_():
#     l1 = [92,72,83,78,70,87,62,80]
#     print(sum(l1)/(len(l1)))
#     l2 = [95,64,61,61,90,88,87,83,90,87]
#     print(sum(l2)/(len(l2)))
#     l3 = [96,72,61,69,71,70,63]
#     print(sum(l3)/(len(l3)))
#     l4 = [68,76,73,86,78,63,75,88,95]
#     print(sum(l4)/(len(l4)))
#     l5 = [85,88,65,94,64,60,87,91,62,78,85,67,90,95]
#     print(sum(l5)/(len(l5)))
#     l6 = [90,61,63,63,78,71,87,93,72,67]
#     print(sum(l6)/(len(l6)))

#     print(sum([78,80.6,71.7,78,79.3,74.5])/6)


if __name__ == '__main__':
    # process_()
    # thread_()
    gen_()