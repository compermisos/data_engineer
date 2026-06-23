import json
from pydantic import BaseModel, EmailStr, PositiveInt, Field, field_validator

# 1. Define your schema
class User(BaseModel):
    name: str
    age: PositiveInt | None = None
    email: EmailStr | None = None

    @field_validator("age", "email" , mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        # Convert empty CSV cells to None so Optional type works
        if v == "":
            return None
        return v

if __name__ == "__main__":
    user_model_schema = User.model_json_schema()  
    print(json.dumps(user_model_schema, indent=2))
