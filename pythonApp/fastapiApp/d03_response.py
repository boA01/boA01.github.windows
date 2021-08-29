from fastapi import FastAPI, Request, Form, File, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates #模板引擎
from tortoise.contrib.fastapi import register_tortoise #将app与数据库绑定
from starlette.responses import StreamingResponse
from pydantic import BaseModel, EmailStr
from typing import Union, List

app = FastAPI()
template = Jinja2Templates("page")

# 数据库的绑定
# register_tortoise(app, 
#                   db_url="mysql://root@118.190.201.50:3306/fastapi",
#                   modules={"modules":["Todo"]},
#                   add_exception_handlers=True,
#                   generate_schemas=True)

todos = ["吃饭", "睡觉", "打游戏"]

# 响应json
@app.get("/user")
def user():
    return JSONResponse(content={"msg":"get user"},
                        status_code=202,
                        header = {"a","b"}
                    )

# 响应html
@app.get("/success")
def user():
    html_content='''
    <html>
        <body>
            <h1 style="color:red">hello man</h1>
        </body>
    </html>
    '''
    return HTMLResponse(content=html_content)

@app.get("/")
def user(req:Request, username='boA'):
    # 从数据库获取tods
    # ORM 获取所有todos
    # todos =await Todo.all()

    return template.TemplateResponse("index.html", context={"request":req, "name":username, "doList":todos})

# 响应重定向
@app.post("/todo/")
def todo(
    content:str=Form(None), 
    file:bytes = File(None),
    fileb:UploadFile = File(None)
):
    # 处理form发来的todo
    global todos
    todos.insert(0,content)

    print(
        {
            "file_size":len(file),
            # "fileb_content_type":fileb.content_type
        }
    )
    # 把数据存储到数据库
    # await  Todo(content=content).save()
    return RedirectResponse("/", status_code=302) #状态码：302->get请求 307->post请求

# 响应file
@app.get("/img")
def imt_file():
    file_path="./static/AC.png"
    return FileResponse(file_path) #filename 需要下载，不加就是在线

# 响应自定义类型

class User(BaseModel):
    type:str = "peple"

class User_in(User):
    id:int
    name:str
    pwd:str
    type:str="user"

class User_out(User):
    id:int
    name:str

class User_pwd(User):
    pwd:str

@app.post("/items", response_model=User_out) #指定返回类型
async def create_user(user:User_in): # 接收类型
    return user # 将接收类型转换后返回

items={
    'A':{"id":1001, "name":"A1", "pwd":"666"},
    'B':{"id":11, "name":"B2", "pwd":"6453"},
    'C':{"id":11, "name":"C2"}
}

@app.post("/items/{dept}", response_model=User_out, response_model_exclude_unset=True)
# 只返回实例有的内容
# response_model_exclude={"pwd"} 排除pwd
# response_model_include=["name", "id"] 返回name，id
async def read_user(dept:str):
    return items.get(dept)

@app.get("/items/{item_id}", response_model=Union[User_out, User_pwd]) # 返回联合类型，简化API接口的多态实现
async def read_item(item_id:str):
    print(items.get(item_id))
    return items.get(item_id)


# 响应状态码
@app.post("/status", status_code=status.HTTP_200_OK)
async def status_num(obj:str):
    return {"status":obj}

# 错误处理
@app.post("/woring")
async def cxce(item:str):
    if item in items:
        return items.get(item)
    raise HTTPException(status_code=404, 
                        detail="type not right",
                        headers={"X-Error":"There goes my error"}) #头部说明，某些安全性问题

# 自定义异常类
class UnicornException(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(req:Request, exc:UnicornException):
    return JSONResponse(
        status_code=110,
        content={"message":f"{exc.name} did somethin."}
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name:str):
    if name!="hello":
        raise UnicornException(name)
    return {"unicorn_name":name}