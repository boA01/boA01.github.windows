
from fastapi import APIRouter
from fastapi import  Depends,HTTPException
from models.crud import *
from models.database import *

usersRouter=APIRouter()

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

# 新建用户
@usersRouter.post("/users/", tags=["users"], response_model=Users)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
        - **email**: 用户的邮箱
        - **password**: 用户密码
    """
    db_crest = get_user_emai(db, user.email)
    if not db_crest:
        return db_create_user(db=db, user=user)
    raise HTTPException(status_code=200, detail="账号不能重复")


@usersRouter.post("/user/item/{user_id}", response_model=List[Items])
def get_user_items(user_id: int, db: Session = Depends(get_db)):
    return get_user_item(db=db, userid=user_id)


# 通过id查询用户
@usersRouter.get("/user/{user_id}", response_model=Users)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="用户查找不到")
    return db_user


# 创建用户的item
@usersRouter.post("/users/{user_id}/items", response_model=Items)
def create_item_user(
    user_id: int,
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)
