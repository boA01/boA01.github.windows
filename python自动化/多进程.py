import multiprocessing as mt #进程模块
import threading as td #线程模块
import time as tm
import os

lock = td.Lock() #创建互斥锁
def music():
    lock.acquire() #上锁
    music_process_id = os.getpid()
    print(music_process_id, 'music')
    for i in range(5):
        print("musicing")
        tm.sleep(0.2)

def play():
    play_process_id = os.getpid()
    print(play_process_id, 'play')
    for i in range(5): 
        print("playing......")
        tm.sleep(0.2)
        # os.kill(play_process_id, 9)

#获取当前进程编号
main_process = os.getpid()
print(main_process,'main')


if __name__ == "__main__":
    #创建子进程,不共享全局变量
    play_process = mt.Process(target = play)
    music_process = mt.Process(target = music)

    #创建子线程,共享全局变量
    # music_thread = td.Thread(target=music)
    # play_thread = td.Thread(target=play)

    play_process.start() #子进程
    # play_thread.join()#线程等待
    music_process.start() #主进程