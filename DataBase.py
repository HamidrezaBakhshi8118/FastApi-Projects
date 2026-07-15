from sqlalchemy import create_engine , Column 
from sqlalchemy.orm import sessionmaker , declarative_base


DATABASE_URL="posgresql://user:password@localhost:5432/dbname"

engine=create_engine(url=DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine)

Base=declarative_base()

Base.metadata.create_all(engine)