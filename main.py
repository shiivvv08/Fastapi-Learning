from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI(title="fastapi tutorial")

@app.get("/")# decorator 
def hello_world():
    return {"hello shivam":"welcome to fastapi tutorial"}

@app.get("/hello/{name}") # path parameter 
def hello_name(name : str): # type hinting
    return {"hello" : name} # query parameter

class Todo(BaseModel):
    id : int
    title : str
    completed : bool

todos = [{"id": 1, "title": "fastapi", "completed": False} , {"id": 2, "title": "learn python", "completed": True}   ]  # in memory database

@app.get("/todo")
def get_todo():
    return todos
    


@app.get("/users")
def get_users(name : str = None): # we give str = none to handle error
    return { "name" : name}

# multi-parameter
@app.get("/items")
def get_items(name : str = None , price : int = 0):
    return {
        "name" : name,
        "price" : price
    }

@app.post("/todo")
def create_todo(todo : Todo):
    todos.append(todo)
    return {"message" : "todo created successfully" , "todo" : todo}


@app.post("/create-user")
def post_user(name : str = None , id : int = 1 , email : str = None):
    return {
        "name" : name,
        "id" : id,
        "email" : email
    }

@app.post("/create-student")
def post_student(student : dict):
    return {
        "message" : "student created successfully !",
        "data" : student
    }
    
#  pydantic model - schema structure whcih defines how data should appear

# nested 

class Address(BaseModel):
    address : str
    pincode : int
    

class Student(BaseModel):
    # key : format pair
    name : str
    age : int
    email : str
    address : Address  #this parameter inherite the base class of Address
    
@app.post("/student-details")
def post_details(student : Student):
    return {
        "message" : "student added successfully",
        "data" : student
    }
    
    
    
    



























if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000 , 
                reload=True)
    
    
    
