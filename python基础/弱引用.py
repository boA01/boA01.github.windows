'''
垃圾回收机制：引用计数为主，标记清除、分代回收为辅
'''
import threading as td
import weakref

class Data:
    def __init__(self):
        ...

# 中间件
class Cacher:
    def __init__(self):
        # self.pool = {}
        # self.pool_key_ref = weakref.WeakKeyDictionary() #键只保存弱引用的映射类
        self.pool_value_ref = weakref.WeakValueDictionary() #值只保存弱引用的映射类
        self.lock = td.Lock()
    
    def get(self, key):
        with self.lock:
            if data := self.pool.get(key):
                return data

            data = Data(key)

            # self.pool[key] = data #直接放入对象
            '''
            有资源泄露风险，字典pool会不停变大，占用内存。
            '''

            # self.pool[key] = weakref.ref(data) #装入对象的弱引用
            '''
            中间件本身不使用对象，所以不应该对数据产生引用。
            弱引用：本身不产生引用计算，当对象的引用计算为零后，自动为空。
            '''

            self.pool_value_ref[key] = data #自动就是对象的弱引用

            return data
