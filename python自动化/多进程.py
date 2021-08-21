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
    #创建子进程,不共享全局变量
    play_process = mt.Process(target = play)
    music_process = mt.Process(target = music)
    
    #获取当前进程编号
    main_process = os.getpid()
    print(main_process,'main')

    play_process.start()
    music_process.start()
    print("玩....",play_process.pid)
    print("音乐", music_process.pid)


def run(n):
        tm.sleep(n)
        return n

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
    test2()
    pass
