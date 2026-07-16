from DataBase import User , SessionLocal
from datetime import datetime

session=SessionLocal()


#new_user=User(first_name = "ali" , last_name= "hosseini" , age = 32 , joined_at = datetime.now())

#session.add(new_user)
#session.commit()

users=session.query(User).all()
print(users)