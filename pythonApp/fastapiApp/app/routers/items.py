from fastapi import APIRouter
from fastapi import  Depends
from models.crud import *
from models.database import *

itemsRouter=APIRouter()

def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# 所有item
@itemsRouter.get("/items/", response_model=List[Items])
def read_items(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    items = get_item(db=db, skip=skip, limit=limit)
    return items