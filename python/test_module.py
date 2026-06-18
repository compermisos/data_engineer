import models.user as m_user
user = m_user.User(**m_user.test_data)  
print(user.id)  
print(user.model_dump()) 
