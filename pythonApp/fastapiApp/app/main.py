from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from aioredis import create_redis_pool, Redis

from routers.user import usersRouter
from routers.items import itemsRouter
from routers.file import fileRouter
from routers.websocket import socketRouter

from models.schemas import UserCreate
from config import *

tags_metadata = [
    {
        "name": "系统接口",
        "description": "用户创建和items创建"
    },
    {
        "name": "items",
        "description": "管理items，你可以查看文档",
        "externalDocs": {
            "description": "使用文档",
            "url": "http://localhost:8000/docs#/Itmes",
        },
    },
]

app = FastAPI(
    # 元数据
    title="系统接口",
    version="0.0.1",
    openapi_tags=tags_metadata,

    # 文档 URL
    docs_url="/openapi", #Swagger UI
    redoc_url="/apidoc" #ReDoc
)

# 页面模板
templates = Jinja2Templates(directory="./page")
# 挂载静态目录
app.mount("/static", StaticFiles(directory="./static"), name="static")

app.include_router(usersRouter, prefix="/user", tags=['users'])
app.include_router(itemsRouter, prefix="/items", tags=['Items'])
app.include_router(fileRouter, prefix="/file", tags=['file'])
app.include_router(socketRouter, prefix="/socket", tags=['socket'])

'''
async def get_redis_pool() -> Redis:
    redis = await create_redis_pool(r"redis://:@"+redishost+":"+redisport+"/"+redisdb+"?encoding=utf-8")
    return redis

@app.on_event("startup")
async def startup_event():
    app.state.redis = await get_redis_pool()

@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()
    await app.state.redis.wait_closed()

@app.get("/test", summary="测试redis")
async def test_redis(request: Request, num: int=Query(123, title="参数num")):
    #  等待redis写入  await异步变同步 
    # 如果不关心结果可以不用await，但是这里下一步要取值，
    # 必须得先等存完值 后再取值
    await request.app.state.redis.set("test", num)
    # 等待 redis读取
    v = await request.app.state.redis.get("test")
    print(v, type(v))
    return {"msg": v}
'''

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@app.post("/token")
def token(user: UserCreate):
    print("----------->", user.email)
    if user.password:
        if user.password == "123456":
            return {"token":user.email+"666", "msg":"pass", "u_name":user.email}
    return {"msg":"fail"}
'''
def token(user: UserCreate, db: Session = Depends(get_db)):
    db_crest = get_user_email(db, user.eamil)
    fake_hashed_password = user.password + "notreallyhashed"
    if db_crest:
        if fake_hashed_password == db_crest.hashed_password:
            return {"token":"leizishuoceshi", "msg":"pass"}
        return {"msg":"fail"}
'''

@app.get("/success")
async def chat(u_name, request: Request):
    return templates.TemplateResponse(
        "success.html",
        {
            "request": request, "u_name": u_name
        }
    )

#接口屏蔽
@app.get("/legacy/", include_in_schema=False)
def get_legacy_data(response: Response):
    headers = {"X-Cat": "leizi", "Content-Language": "en-US"}
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>r
    </shampoo>
    """
    response.set_cookie(key="message", value="hello")
    
    return Response(
        content=data, 
        media_type="application/xml", 
        headers=headers
    )

# if __name__ == '__main__':
#     import uvicorn

#     uvicorn.run(
#         app='main:app',
#         host="127.0.0.1",
#         port=8000,
#         reload=True,
#         debug=True
#     )