from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers.user import usersRouter
from routers.items import itemsRouter

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
app.include_router(itemsRouter, prefix="/sendtxt", tags=['bgs'])

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@app.get("/legacy/")
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