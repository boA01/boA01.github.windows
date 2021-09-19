class O():
    name = "D_class" # 类属性
    __solts__ = ("ip") # 槽，限制当前类实例绑定的属性，子类不影响

    def __new__(cls): # 类方法（特殊，不用加装饰器）
        print("构造方法")
        return super().__new__(cls)

    def __init__(self, id): # 实例方法
        print("初始化方法")
        self.id = id # 实例属性

    @staticmethod
    def static_get(): # 静态方法——类中的函数
        print("静态方法")

    @classmethod
    def class_get(cls): # 类方法，不能访问实例属性
        print(cls.name) # 访问类属性
    
    def test(self): #实例方法，类名不可直接调用
        print("O test")

    def __len__(self): #len(o) == o.len()
        return 10
    
    def __str__(self):
        return f"id:{self.id}"

class A_Mixln():
    def hehe(self):
        return "呵呵呵"

class B_Mixln():
    def haha(self):
        return "哈哈哈"

    def hehe(self):
        return "hehehe"

class C(O, A_Mixln, B_Mixln): #print(C.__mro__)继承顺序：广度优先
    name = "C_class" #类属性
    a = 0
    __solts__ = ("color") #可以绑定ip（继承的）和color
    
    def __init__(self, name=None, age=None, id=None, path=None):
        O.__init__(id) 
        self._name = name #实例属性, _"保护"
        self.__age = age #实例属性, __私有；类外访问：c._C__age
        self.__path = path

    def set_age(self, age):
        if not (age>0 or age<100):
            raise ValueError("error")
        self.__age = age
        
    def get_age(self):
        return self.__age

    def test(self):
        print("C test")  #多态，重写父类方法
    
    def p(self):
        print("O->C")

    @property #变属性，getter方法（只读）
    def sex(self):
        return self._sex
    
    @sex.setter #变setter方法（可写）
    def sex(self,value):
        if not (value=="男" or "女"):
            raise ValueError("error")
        self._sex=value

    @property #只读属性
    def birth(self):
        return 2021 - self.__age;

    # 可迭代
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a+=1
        if self.a<6:
            raise StopIteration()
        return self._name
    
    # 序列化容器
    def __getitem__(self,n):
        a,b=1,1
        if isinstance(n,int): #n是数字
            for i in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice): #n是切片
            start = n.start
            stop = n.stop 
            if start is None:
                start = 0
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a,b=b=a+b
            return L
    
    # __setitem()__, __delitem__()

    # 上下文管理器
    def __enter__(self):
        print("int __enter__")
    def __exit__(self, exception_type, exception_value, traceback):
        print("int __exit__")
        if exception_type is None:
            print("[in __exit__] Exited without exception")
        else:
            print("[in __exit__] Exited with exception: %s" % exception_value)
            return False
            
    # 调用不存在的属性或方法时被调用 s.qq s.qq()
    def __getattr__(self, attr):
        if attr == "qq":
            return "66666666" # return lambda:"666"
        return f"no extis {attr}"

    def __str__(self):
        return super().__str__()+f" naem:{self._name} age:{self.__age}"

    __repr__ = __str__ 
    #让c 和 print(c)一样打印字符串；
    #前者为了调试，是开发者看见的，后者用户看见的

    # 实例本身调用，c()
    def __call__(self,path=None):
        print(f"{self.__class__.__name__}")
        # return C('%s/%s' % (self.__path, path))

# type()动态创建类，class就是调用type()
def fn(self, name="world"):
    print(f"hello {name}")

Hello = type("Hello",(object,),dict(hello=fn))

# metaclass(元类)创建或魔改类,必须从type派生
# cls：当前类，name：类名，bases：父类集合，attrs：方法集合
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs["add"] = lambda self, value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

# metaclass：关键字，指：用ListMeatclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass


################动态内存交换
'''
c = C()
isinstance(c,O) c是O类么
hasattr(c,"id") c有id属性么 *******大用********
setattr(c,"ip","xxx") 设置一个c的属性
getattr(c,"sex",'404') 获取c的属性，没有默认返回404
delattr(c,"name") 删除c的属性

实例绑定属性
c.ip = "xxx" 

from types import MethodType as mt

def get_ip(self, ip):
    self.ip = ip

实例绑定方法
c.get_ip = mt(get_ip,c)

类绑定方法
C.get_ip = get_ip
'''

if __name__ == "__main__":
    # 测试多态
    def test_twice(o):
        o.test()

        """
        print(__file__) >>>面向对象.py
        print(sys.argv)：获取命令行参数
        
        int main(int argc, char* argv[]){
            while(argc-- > 1)
                printf("%s\n",*++argv)
        }
        """