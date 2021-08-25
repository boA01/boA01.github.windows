from fastapi import FastAPI, Query, Path, Body, Header #Query 参数验证，Path 路径验证
from enum import Enum # 枚举
from pydantic import BaseModel, HttpUrl #模板
from typing import List

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

app = FastAPI()

# 只能接收固定参数，枚举类Name
@app.get("/hello/{who}")
async def get_str(who:Name):
    if who == Name.A:
        return f"你好 {who}"
    if who.value == "哈哈哈":
        return f"你好 哈哈哈"
    return f"你好 憨憨"

# 接收item对象
@app.post("/items")
async def create_item1(item:Item):
    return item.dict()

# 更新
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
    # print(result)
    return result

@app.get("/")
async def main():
    return "你好 FastAPI"

# if __name__=="__main__":
    # import uvicorn

    # uvicorn.run(app,host="127.0.0.1", port=8000)