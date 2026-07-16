from sqlalchemy import create_engine , Column , Integer , String , UUID , BOOLEAN ,DateTime
from sqlalchemy.orm import sessionmaker , declarative_base 


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



Base.metadata.create_all(engine)