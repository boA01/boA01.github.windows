import time

def repeat(nums=3):
    def decorator_repeat(func):
        def wrapper(*args,**kw):
            print("start")
            for i in range(nums):
                func(args, kw)
            print("end")
        return wrapper
    return decorator_repeat

@repeat(2)
# @decorator_repeat
def func1(args, kw):
    print("kkk",args, kw)

def say_hello():
    def wrapper(*args, **kw):
        print("hello world")
        


if __name__=="__main__":
    func1(1,2,3,4,a=1,b=2)