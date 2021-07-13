import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    assert n!=0,"n is zero" #断言，用于调试，代替print(),断言开关：-O
    # logging.info(f"n={n}")
    return 10 / n

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e) #打印错误日志
        # raise #抛出异常

main()
print('END')