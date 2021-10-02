import time

# 函数饰器
def decorator_args(s=1): #接收装饰器参数
    def decorator(fn): #接收方法
        start = 0
        def wrapper(*args, **kwargs): #实现逻辑
            nonlocal start #嵌套变量
            now = time.time()
            if now-start>s:
                fn(*args, **kwargs) #调用方法
                start = time.time()
            else:
                print(f"再坚持{s-int(now-start)}s", end='\r')
        return wrapper
    return decorator

@decorator_args(5)
def fun1():
    print("我要玩....")

# 类装饰器
class logger1():
    def __init__(self, fn): #接收方法
        self.fn = fn 
    def __call__(self, *args, **kwargs): #实现逻辑
        return self.fn(*args, **kwargs)

class logger2():
    def __init__(self, y=2): #接收装饰器参数
        self.y = y
    def __call__(self, func): #接收方法
        def wrapper(*args, **kwargs): #实现逻辑
            for i in range(self.y): #执行y次
                ret = self.fn(*args, **kwargs)
            return ret
        return wrapper

#@logger1
@logger2(3)
def fn2():
    pass

if __name__=="__main__":
    fun1()
    time.sleep(1)
    fun1()
    time.sleep(1)
    fun1()
    time.sleep(1)
    fun1()
    time.sleep(1)
    fun1()
    time.sleep(1)
    fun1()