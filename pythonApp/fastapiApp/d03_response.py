from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates #模板引擎
from tortoise.contrib.fastapi import register_tortoise #将app与数据库绑定

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

# 响应file
@app.get("/img")
def user():
    file_path="./static/AC.png"
    return FileResponse(file_path) #filename 需要下载，不加就是在线

# 响应重定向
@app.post("/todo/")
def todo(content:str=Form(None)):
    # 处理form发来的todo
    global todos
    todos.insert(0,content)

    # 把数据存储到数据库
    # await  Todo(content=content).save()

    return RedirectResponse("/", status_code=302) #状态码：302->get请求 307->post请求