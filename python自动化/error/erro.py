import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    assert n!=0,"n is zero" #断言，用于调试，代替print(),断言开关：-O
    # logging.info(f"n={n}")

    #******************
    if n==0:
        raise ValueError(f"n={n}") #抛出异常
    #******************
    return 10 / n

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e) #打印错误日志
    
    #******************
    except ValueError as e:
        print(repr(e)) #打印异常注释
    #******************
    
main()
print('END')