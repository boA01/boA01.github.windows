import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
if __name__=='__main__':

    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr='127.0.0.1'
    print('Connect to server %s...'%server_addr)
    #端口设置和task_master.py中一样
    m=QueueManager(address=(server_addr,5000),authkey=b'abc')
    #连接网络
    m.connect()

    task=m.get_task_queue()
    result=m.get_result_queue()

    for i in range(10):
        try:
            #接收任务队列中的数据
            n=task.get(timeout=1)
            print('Run task %d*%d'%(n,n))
            r='%d*%d=%d'%(n,n,n*n)
            time.sleep(1)
            #放进结果队列
            result.put(r)
        except Queue.Empty:
            print('task queue is empty')         
    print('work done')