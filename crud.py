from DataBase import User , SessionLocal
from datetime import datetime
from sqlalchemy import select ,func
session=SessionLocal()


#new_user=User(first_name = "ali" , last_name= "hosseini" , age = 32 , joined_at = datetime.now())
#new_user2=User(first_name = "hossein" , last_name= "rezaii" , age = 42 , joined_at = datetime.now())
#new_user3=User(first_name = "reza" , last_name= "bakhshi" , age = 23 , joined_at = datetime.now())

#all_users=[new_user,new_user2,new_user3]

#session.add_all(all_users)
#session.commit()

#users=session.query(User).all()
#print(users)


#user = session.query(User).where(User.first_name.like("ali")).all()


user = session.query(func.max(User.age)).scalar()
print(user)