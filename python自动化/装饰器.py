import time
def my_decorator(func):
    def wrapper(*args,**kw):
        print(args)
        print("start")
        func(args,**kw)
        print("end")
    return wrapper

@my_decorator
def func1(args,**kw):
    print(args)
    print("hello world")

def say_hello():
    def wrapper(*args, **kw):
        


if __name__=="__main__":
    func1(1,2,3,4)

