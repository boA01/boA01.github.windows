from concurrent.futures import ProcessPoolExecutor as ppExecutor
import multiprocessing as mt #进程模块
import time as tm
import os

def test():
    print("我不会被复制")

    pid = os.fork()
    '''
    fork()，linux和unix下使用
    复制父进程，父子都运行，子进程运行fork()后面的代码
    '''
    print("我会被复制")

    if pid == 0:
        print(f"子进程{os.getpid()}的父进程是{os.getppid()}")
        pass
    else:
        print(f"父进程{pid}")

    tm.sleep(2) #父进程等待子进程结束


def music():
    print('music', os.getpid())
    for i in range(5):
        print("musicing")
        tm.sleep(0.2)

def play():
    print('play', os.getpid())
    for i in range(5): 
        print("playing......")
        tm.sleep(0.2)
        # os.kill(play_process_id, 9)

def test1(): 
    play_process = mt.Process(target = play)
    music_process = mt.Process(target = music)
    
    #获取当前进程编号
    main_process = os.getpid()
    print(main_process,'main')

    play_process.start()
    music_process.start()
    print("玩....",play_process.pid)
    print("音乐", music_process.pid)


# 进程间通信：管道<pipe，fifo>，消息队列<queue>，信号，数据共享<meanager>，套接字<网络，UNIX域>
#队列(Queue)
def foo(q):
    tm.sleep(1)
    print("子进程")
    q.put(123)
    q.put("hello")

def test3():
    q = mt.Queue()
    p = mt.Process(target = foo,args=(q,))
    p.start()
    print("主进程")
    print(q.get())
    print(q.get())

#管道(pipe，只能用于两个进程间通信，性能较高)
def child(c_conn):
    print("子进程....")
    while True:
        try:
            data = c_conn.recv() # 接收数据
            print(data)
        except Exception as e:
            print(e)
            c_conn.close()# 关闭管道
            break
    pass

def parent(p_conn):
    print("主进程....")
    with p_conn:
        for i in range(10):
            print(f"发送：{i}")
            p_conn.send(i) # 发送数据
    pass

def test4():
    parent_conn, child_conn = mt.Pipe() #创建双向管道

    c1 = mt.Process(target=child, args=(child_conn,))
    c1.start()

    parent(parent_conn)

    parent_conn.close() # 关闭管道
    child_conn.close()

    c1.join() #等待子进程

    print("end")
    pass

#数据共享(manager)
def f(d,l,n):
    d[n] = "O"
    d[0.1]="A"
    l.append(n)

    print(l)
    print(d)
    print("_________________")
    pass

def test5():
    manager = mt.Manager()
    d = manager.dict() #创建共享字典
    l = manager.list(range(3)) #创建共享列表

    p_list = []
    for i in range(3):
        p = mt.Process(target=f, args=(d, l, i)) #开启子进程
        p.start()
        p_list.append(p)
    
    for p in p_list:
        p.join()

    print("++++++++++++")
    print(d)
    print(l)
    print("end")


############进程同步(协同步调，读写)###############
def fun(lock,l,i):
    with lock:
        print(f"{os.getpid()}：{l}")
        tm.sleep(2)
        l[0]+=i
        print(f"{os.getpid()}：{l}")

def test6():
    lock = mt.Lock()
    manager = mt.Manager()
    l = manager.list([100000])

    mt.Process(target=fun, args=(lock,l,1)).start()
    mt.Process(target=fun, args=(lock,l,2)).start()
    mt.Process(target=fun, args=(lock,l,1)).start()

    l[0]+=1
    tm.sleep(7)
    print(f"结果：{l}")


# 进程池（共享数据用manager修饰）
def run(n):
        tm.sleep(n)
        return n #进程通信

def test2():
    #使用进程池
    pool = mt.Pool(3) #最大值与核数相同最优；cpu核数：mt.cpu_count()

    # result = pool.apply_async(run,args=(3)) #异步提交
    # pool.close() #！！！！重点，满了就关闭进程池！！！！！
    # pool.join() #等待所有进程完成
    # print(result.get()) #得到返回值

    #imap() #按可迭代对象输入顺序
    # for result in pool.imap(run, [1,3,2]):
    #     print(f"sleep {result} sucess")
    
    #imap_unordered() #按结束时间顺序
    for result in pool.imap_unordered(run, [1,3,2]):
        print(f"sleep {result} sucess")


if __name__ == "__main__":
    # test()
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()
    pass
