'''
t	文本模式 (默认)。
r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（Python 3 不支持）。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。f.tell() f.seek()
也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
'''

# 文件
def f1(file,mode="r",encoding="gbk",errors="ignore"):
    with open(file, mode, encoding, errors) as f:
        print(f.read())

    '''
    try:
        f=open(file,mode="a",encoding="utf-8")
        f.write("Hello world")
    except Exception as e:
        print(e)
    finally:
        f.close()
    '''


from io import StringIO,BytesIO

def f2():
    f = StringIO()
    f.write("hello")
    f.write(" ")
    f.write("world")
    # print(f.getvalue())
    while s:= f.readline().strip():
        print(s.strip())

def f3():
    f = BytesIO()
    f.write("中文".encode("utf-8"))
    print(f.getvalue())

import os

os.name()
os.uname()
os.environ()
os.environ().get("PATH")
os.path.abspath(".")
os.getcwd()
os.chdir()
os.listdir()
os.path.join()
os.path.split()
os.path.splitext()
os.path.isdir()
os.mkdir()
os.rmdir()
os.path.isfile()
os.remove()
os.rename()

import shutil

shutil.copyfile()

import pickle
import json
d = dict(name="boA", age=21)
# 序列化：把变量从内存中变成可存储或传输的过程
josn_str = json.dumps(d) #str
# json.dumps(s,default=student2dict) #序列化对象是，添加转dict函数
'''
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
    }
'''
# json.dumps(s, default=lambda obj: obj.__dict__) #偷懒方法
pickle.dumps(d) #>>>bytes

with open(file="dump.txt",mode='wb') as f:
    json.dump(d,f) #file-like Object
    # pickle.dump(d,f)

# 反序列化
json.loads(josn_str)
# print(json.loads(json_str, object_hook=dict2student)) #编写转换函数
'''
def dict2student(d):
     return Student(d['name'], d['age'])
'''
with open("dump.txt","rb") as f:
    d = json.load(f)
    # d = pickle.load(f)
    print(d)



