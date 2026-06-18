import .model_pydantic
user = model_pydantic.User(**model_pydantic.test_data)  
print(user.id)  
print(user.model_dump()) 
