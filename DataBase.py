from sqlalchemy import create_engine , Column , Integer , String , BOOLEAN ,DateTime , ForeignKey
from sqlalchemy.orm import sessionmaker , declarative_base , relationship


DATABASE_URL="postgresql://postgres:147852@localhost:5432/fastapi_course"

engine=create_engine(url=DATABASE_URL,echo=True)
SessionLocal = sessionmaker(autoflush=False,bind=engine)

Base=declarative_base()




class User(Base):

    __tablename__= "users"

    id = Column(Integer , primary_key=True , autoincrement=True)
    first_name=Column(String(length=30) , nullable=True)
    last_name=Column(String(length=30) , nullable=True)
    age = Column(Integer , nullable=True)
    is_active= Column(BOOLEAN,default=True)
    joined_at = Column(DateTime)

    addresses = relationship("Addres", back_populates="user")


    def __repr__(self):
        return f"User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')"

class Addres(Base):
    __tablename__= "addres"

    id = Column(Integer , primary_key=True , autoincrement=True)
    user_id = Column(Integer , ForeignKey("users.id"))
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Addres(id={self.id}, city='{self.city}', state='{self.state}', zip_code='{self.zip_code}')"

Base.metadata.create_all(engine)