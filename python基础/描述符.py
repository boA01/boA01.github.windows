'''
描述符协议
实现__set__(), __get__, __delete__()至少一个方法
'''

class Score():
    def __init__(self, default):
        self.name = default

    def __set__(self, instance, value):
        if 0<=value<=100:
            instance.__dict__[self.name]=value
        else:
            raise ValueError("value error")
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __delete__(self):
        del self._score

class Student():
    math = Score("math")
    chinese = Score("Chinese")
    cs = Score("cs")

    def __init__(self, *args):
        self.name = args[0]
        self.math = args[1]
        self.chinese = args[2]
        self.cs = args[3]

    def __str__(self):
        return f"name:{self.name}\
            math:{self.math}\
            chinese:{self.chinese}\
            cs:{self.cs}"


if __name__ == "__main__":
    s1 = Student("xm", 66, 34, 45)
    s2 = Student("xh", 69, 39, 49)
    print(s1)
    print(s2)