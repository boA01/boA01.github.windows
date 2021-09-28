import asyncio

############ 生成器
# def fn():
#     yield range(10)
#     yield from range(10)

############ 协程
async def fn1(delay):
    await asyncio.sleep(delay)
    print("hello")

async def fn2(delay):
    await asyncio.sleep(delay)
    print("world")

async def main():
    # 串行
    # await fn1(2)
    # await fn2(1)

    # 并发
    '''
    通过 asyncio.create_task(coro, *, name=None)
    等函数被打包为一个 任务，该协程将自动排入日程准备立即运行
    '''
    # task = asyncio.ensure_future(coro()) # 3.7以下
    # t1 = asyncio.create_task(fn1(2))
    # t2 = asyncio.create_task(fn2(1))
    # await t1
    # await t2

    # 并发运行任务
    #  awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
    await asyncio.gather(
        fn1(2),
        fn2(1),
        fn2(2),
    )

    print("end")

if __name__=='__main__':
    # print(next(fn()))
    asyncio.run(main())