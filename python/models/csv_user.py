from pydantic import BaseModel, EmailStr, PositiveInt

# 1. Define your schema
class User(BaseModel):
    name: str
    age: PositiveInt
    email: EmailStr
