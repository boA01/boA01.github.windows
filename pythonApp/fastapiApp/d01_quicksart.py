from fastapi import FastAPI 
import uvicorn

app = FastAPI()

# 字符串接口
@app.get("/")
def index():
    '''
    首页接口
    '''
    return "hello fastapi"

# json接口
@app.get("/user")
def users():
    '''
    用户接口
    '''
    return {"msg":"get all users", "code":2021}

# 列表接口
@app.get("/projects")
def projects():
    '''
    内容接口
    '''
    return ["A","B","C"]

if __name__ == "__main__":
    '''
    开发文档
    '''
    uvicorn.run(app)