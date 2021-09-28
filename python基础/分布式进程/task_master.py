import random,time,queue
from multiprocessing.managers import BaseManager
#发送任务队列
task_queue=queue.Queue()
#接收结果队列
result_queue=queue.Queue()

#继承BaseManager
class QueueManager(BaseManager):
    pass
def return_task_queue():
    #global 用于函数内部，修改全局变量的值
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue
if __name__=='__main__':
    #将两个Queue注册到网络上，callable参数关联Queue对象
    #！win10中callale不对lambda匿名函数做处理  
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    #绑定端口5000，这5000怎么来的？两个文件中的端口一样就行！，设置验证码abc
    #通过QueueManager将Queue暴露出去
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    manager.start()
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    #放10个任务进去
    for i in range(10):
        n=random.randint(0,1000)
        print('Put task %d...'%n)
        #将数据放到任务队列
        task.put(n)
    #取任务执行结果
    print('Try get results...')
    for i in range(10):
        #从结果队列中取结果
        #等待10是因为计算需要时间
        r=result.get(timeout=10)
        print('REsult:%s'%r)
    #关闭
    manager.shutdown()
    print('master end')