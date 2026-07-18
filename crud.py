from DataBase import User , SessionLocal , Addres
from datetime import datetime
from sqlalchemy import select ,func
from sqlalchemy.sql import text
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


#user = session.query(func.max(User.age)).scalar()
#print(user)

#query = text("SELECT * FROM  users")
#result=session.execute(query).all()
#print(result)


#address_1 = Addres(city="karaj",state="Alborz",zip_code="2002")
#address_2 = Addres(city="tehran",state="tehran",zip_code="3003")
#address_3 = Addres(city="mashhad",state="khorasan_razavi",zip_code="4004")

#all_addresses = [address_1,address_2,address_3]

#session.add_all(all_addresses)
#session.commit()

#user = session.query(User).where(User.first_name.like("ali")).one_or_none()

#address = session.query(Addres).where(Addres.user_id==user.id).all()
#print(address)



#result = session.query(User).join(User.addresses).where(User.first_name == "ali").all()
#print(result)


users = session.query(User).join(User.addresses).where(Addres.city == "tehran").all()
print(users)