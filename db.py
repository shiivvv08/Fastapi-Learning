from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI , Depends , HTTPException


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
   
Base.metadata.create_all(bind=engine) #db me table create krne ke liye


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        
# @app.get("/")

# def get_home(db : Session = Depends(get_db)):
#     return {
#         "message": "sqlite connected successfully"
#     }
    

#  crud operation

# create api

@app.post("/todos")
def create_todos(title:str , db: Session = Depends(get_db)):
    todo = Todo(title=title , completed = "fasle")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message" : "todo created successfully",
        "data" : todo
    }


# read api 
@app.get("/todos")
def get_todos(db : Session = Depends(get_db)):
    
    todos = db.query(Todo).all()
    return {
        "message" : "todos retrived successfully",
        "data" : todos
    }

# by id read api
@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id : int , db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404 , details="todo not found")
    return {
        "message": "todo retrived successfully",
        "data" : todo
    }
    
# update api
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int , title : str , completed : str , db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404 , details="todo nhi bana hai")
    todo.title = title
    todo.completed = completed
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message" : "todo updated successfully",
        "data" : todo
    }
    
# delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id : int , db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo :
        raise HTTPException(status_code=404 , details="todo nhi mila ")
    
    db.delete(todo)
    db.commit()
   
    return{
        "message": "todo deleted successfully",
    }
    
    
