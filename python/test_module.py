import models.user as m_user
user = m_use.User(**m_user.test_data)  
print(user.id)  
print(user.model_dump()) 
