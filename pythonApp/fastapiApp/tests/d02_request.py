from fastapi import FastAPI, File, UploadFile, Query, Header, Body, Path, Form #Query 参数验证，Path 路径验证
from enum import Enum # 枚举
from pydantic import BaseModel, HttpUrl #模板
from typing import List

app = FastAPI()

class Name(str,Enum): # 数据字典
    A = "嘿嘿嘿"
    B = "哈哈哈"
    C = "呵呵呵"

class Item(BaseModel):
      name:str
      price:float

class Image(BaseModel):
    name:str
    url:HttpUrl

#             获取url参数
# http://127.0.0.1:8000/user1/666
@app.get("/user1/{id}")
def get_user1(id):
    return {"id":id}

#             接收请求头数据
# http://127.0.0.1:8000/user2?id=666
@app.get("/user2")
def get_user2(id,token=Header(None)):
    return {"id":id, "token":token}
    
#             接收json数据
@app.api_route("/login_json",methods=('POST','PUT'))
def login_json(data=Body(None)):
    return {"data":data}

#             接收form数据
@app.post("/login_form")
def login_form(userName=Form(None), userPwd=Form(None)):
    return {"data":{"name":userName,"passwd":userPwd}}

#             接收字文件，两种形式
@app.post("/upload_file")
def upload_file(file:bytes=File(...), fileb:UploadFile=File(...)):
    return {
        "file_size":len(file),
        "fileb_content_type":fileb.content_type
    }

"""
OPTIONS：返回特点资源所支持的请求方法
HEAD：索要和get一致的响应，响应体不返回
GET：在URL中传递参数(只能url编码)，有长度限制，会被保存在浏览器历史记录中；产生一个TCP数据包；查看
POST：在body里传递参数(多种编码)；产生两个TCP数据包；同一条数据重复post3次，数据产生3条；创建
PUT：在body里传递参数(多种编码)；同一条数据重复put3次，数据不改变；更新
DELETE：在body里传递参数(多种编码)；删除标识的资源；删除
TRACE：回显服务器收到的请求；测试或诊断
CONNECT：预留给能将连接改为管道方式的代理服务器
"""

# 只能接收固定参数，枚举类Name
@app.get("/hello/{who}")
async def get_str(who:Name):
    if who == Name.A:
        return f"你好 {who}"
    if who.value == "哈哈哈":
        return f"你好 哈哈哈"
    return f"你好 憨憨"

# 规则
@app.put("/items/{item_id}")
async def create_item2(images:List[Image],
                        user_agent:str=Header(None),
                        x_token:List[str]=Header(None),
                        # 获取请求头，留意 关键字
                        item:Item=Body(...,embed=True),
                        # embed：对象嵌入，若有如下行，不写会自动嵌入；可用于ajax请求
                        importance:int = Body(...),
                        # 单个body参数，不是json对象，可申明为body对象
                        item_id:int=Path(..., title="To put", ge=0, lt=100),
                        #Path() 路径规则：ge：大于等于，gt：大于
                        passwd:str=Query(None, min_length=1, max_length=6, regex="^1"),
                        # Query() 参数规则：None 选填项，... 必填项，deprecated=True 弃用
                        hobbyList:List[str]=Query(["play", "eat"], alias="hobbies")):
    result = {"id":item_id, **item.dict()}
    if passwd:
        result.update({"pwd":passwd})
    if hobbyList:
        result.update({"hobbyList":hobbyList})
    return result


# if __name__=="__main__":
    # import uvicorn

    # uvicorn.run(app,host="127.0.0.1", port=8000)