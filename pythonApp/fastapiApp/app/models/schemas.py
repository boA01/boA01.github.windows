'''
模型验证
'''
from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Items(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    """
    请求模型验证：
    email:
    password:
    """
    password: str

class Users(UserBase):
    """
    响应模型：
    id:email: is_active并且设置orm_mode与之兼容
    """
    id: int
    is_active: bool
    items: List[Items] = []

    class Config:
        orm_mode = True