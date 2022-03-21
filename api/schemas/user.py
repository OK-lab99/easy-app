from pydantic import BaseModel, EmailStr


#レスポンスbodyをUserBaseで定義
class UserBase(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = True


#post(crudで使う)
class UserCreate(UserBase):
    name: str
    email: EmailStr
    password: str

#put(crudで使う)
class UserUpdate(UserBase):
    password: str | None = None

#DBに格納するための型を定義(レスポンスbodyで使う)
class UserInDBBase(UserBase):
    id: int
    class Config:
        orm_mode = True

#レスポンスbodyで使うスキーマ
class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str