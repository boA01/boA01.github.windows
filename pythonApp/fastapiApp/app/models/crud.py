'''
数据库操作相关
'''
from sqlalchemy.orm import Session
from models.models import  *
from models.schemas import *

# 通过id查询用户
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_emai(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()

# 新建用户
def db_create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新
    return db_user
    
def get_item(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_user_item(db:Session,userid:int):
    user=db.query(User).filter(User.id==userid).first()
    return  db.query(Item).filter(Item.owner==user).offset(1).limit(1).all()

# 新建用户的item
def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item