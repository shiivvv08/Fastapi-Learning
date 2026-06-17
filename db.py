from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI

app = FastAPI()


DATABASE_URL = "sqlite:///.//test.db"

engine = create_engine(
    DATABASE_URL ,
    connect_args={"check_same_thread": False}
    
)

session_local = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(String)
   
Base.metadata.create_all(Bind=engine)

 
    
