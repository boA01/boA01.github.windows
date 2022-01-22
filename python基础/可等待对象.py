#######方式一
from greenlet import greenlet

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()
    print(3)

def func2():
    print(3)
    gr1.switch()
    print(4)

def test1():
    gr2 = greenlet(func2)
    gr1 = greenlet(func1)
    
    gr1.switch()

#######方式二
def func3():
    yield 1
    # yield range(10)
    # yield from range(10)
    yield from func4()
    yield 2

def func4():
    yield 3

def test2():
    fn = func3() #生成器
    for i in fn:
        print(i)

#######方式三

#######方式四
import asyncio
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) #替换原事件循环

async def fn1(delay):
    print(1)
    await asyncio.sleep(delay) #遇到阻塞，自动切换到下一个
    print(2)

async def fn2(delay):
    print(3)
    await asyncio.sleep(delay)
    print(4)

async def main():
    # 串行
    # await fn1(2)
    # await fn2(1)

    # 并发
    # await asyncio.wait([fn1(2), fn2(1)]) #放协程对象
    '''
    Task对象
    通过 asyncio.create_task(coro, *, name=None)等函数被
    打包为一个 任务，该协程将自动排入日程准备立即运行；3.7以
    下用asyncio.ensure_future(coro())

    await asyncio.wait(tasks) #放Task对象
    '''
    #与协程对象比较
    # t1 = asyncio.create_task(fn1(2))
    # t2 = asyncio.create_task(fn2(1))
    # await t1
    # await t2

    # 并发运行任务
    # await asyncio.gather(*aws, loop=None, return_exceptions=False)
    # await asyncio.gather(
    #     fn1(2),
    #     fn2(1),
    #     # fn2(2),
    # )

    print("end")

if __name__=='__main__':
    # gr1 = greenlet(func1)
    # gr2 = greenlet(func2)
    # gr1.switch()

    # test2()

    # 事件循环（调度）
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait([func1(2), func2(1)]))
    # loop.close()

    # 任务列表
    asyncio.run(main())