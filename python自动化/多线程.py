import threading as td #线程模块
from concurrent import futures
import time

class GetDetailHtml(td.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(td.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    
    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

def test1():
    thread1 = GetDetailHtml("get_deatail_html")
    thread2 = GetDetailUrl("get_deatail_url")
    
    # thread1.setDaemon(True) # 设置守护线程，主线程退出，子线程直接结束
    
    thread1.start()
    thread2.start()

    # thread2.join() #阻塞，主线程等待子线程执行完成

    print("end")


############线程同步###############
# 通过互斥锁完成
'''
错误做法
class XiaoAi(td.Thread):
    def __init__(self, lock):
        super().__init__(name="小爱")
        self.lock = lock
    
    def run(self):
        self.lock.acquire() #获得锁
        print("在")
        self.lock.release() #释放锁

        self.lock.acquire() #获得锁
        print("你说")
        self.lock.release() #释放锁

class TianMao(td.Thread):
    def __init__(self, lock):
        super().__init__(name="天猫")
        self.lock = lock
    
    def run(self):
        self.lock.acquire() #获得锁
        print("小爱同学")
        self.lock.release() #释放锁

        self.lock.acquire() #获得锁
        print("回答我个问题吧")
        self.lock.release() #释放锁

def test2():
    lock = td.Lock() # 锁
    xiaoai = XiaoAi(lock)
    tianmao = TianMao(lock)

    tianmao.start()
    xiaoai.start()
'''

# 通过condition完成同步
class XiaoAi(td.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond
    
    def run(self):
        with self.cond: #相当于用self.cond.acquire和self.cond.release()包起来
            self.cond.wait()
            print(f"{self.name}：在")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}：你说")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}：2")
            self.cond.notify()

class TianMao(td.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫")
        self.cond = cond
    
    def run(self):
        with self.cond:
            print(f"{self.name}：小爱同学")
            self.cond.notify() #调用等待线程
            self.cond.wait() #等待

            print(f"{self.name}：回答我个问题吧")
            self.cond.notify() #调用等待线程
            self.cond.wait() #等待

            print(f"{self.name}：1+1=")
            self.cond.notify() #调用等待线程
            self.cond.wait() #等待

def test3():
    cond = td.Condition()
    #condition有两层锁，
    #底层锁在线程调用wait方法时释放
    #上面的锁会在每次调用wait时分配一把并放入到cond的等待队列中，等notify方法唤醒
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    xiaoai.start() #小爱先进入等待
    tianmao.start()


#event同步对象
class Boss(td.Thread):
    def __init__(self,event):
        super().__init__()
        self._event = event

    def run(self):
        print("今晚加班")
        self._event.set() #将等待线程(worker)的False状态改为True
        
        time.sleep(1)
        print("22:00到了，就下班")
        self._event.set()

class Worker(td.Thread):
    def __init__(self,event):
        super().__init__()
        self._event = event

    def run(self):
        self._event.wait() #默认为False
        # print(_event.is_set) #查看状态
        print("哎，命苦")
        self._event.clear() #清除设置过得状态，恢复为False

        self._event.wait()
        print("happy.....")

def test6():
    event = td.Event()

    b = Boss(event)
    w = Worker(event)

    w.start()
    b.start()


# 信号量，semaphore 用于控制进入数量的锁
# 文件，多个线程多一个文件
class HtmlSpider(td.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print(f"got {self.url} html text success")
        self.sem.release() #释放锁

class UrlProducer(td.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(10):
            self.sem.acquire() #上锁，对sem--
            html_thread = HtmlSpider(f"https://baidu.com/{i}", self.sem)
            html_thread.start()
        pass

def test4():
    sem = td.Semaphore(3) # 允许的最大并发数
    urlProducer = UrlProducer(sem)
    urlProducer.start()

# 线程池
# 主线程中可以获取某个线程的状态或者某个任务的状态，以及返回值
# 当一个线程完成时，主线程立即知道
# futures可以让多线程和多进程编码接口一致

def get_html(times):
    time.sleep(times)
    print(f"got html text {times} success")
    return times

def test5():
    excutor = futures.ThreadPoolExecutor(max_workers=2)
    
    '''
    task1 = excutor.submit(get_html,(3))
    task2 = excutor.submit(get_html,(2))

    print(task1.done()) #任务是否完成
    print(task1.result()) #任务的return
    print(task2.cancel()) #取消任务（成功，运行中不能）
    '''

    urls = [2,1,3,4]

    #写法一
    all_task = [excutor.submit(get_html,url) for url in urls]
    futures.wait(all_task) # 等待所有线程结束，才继续向下
    
    for future in futures.as_completed(all_task): #as_completed()生成 过滤done()为False 的迭代器
        data = future.result()
        print(f"get {data} page success")
    '''

    #写法二
    for data in excutor.map(get_html(), urls):
        print(f"get {data} page")
    '''

if __name__=="__main__":
    # test()
    # test3()
    # test4()
    # test5()
    test6()