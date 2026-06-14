from fastapi import FastAPI , status , HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="fastapi crud operations")

todos = []

class Todo(BaseModel):
    # key : value
    id : int
    title : str
    completed : bool
    
@app.post("/todo")
def post_todo(todo : Todo):
    todos.append(todo)
    return {
        "message" : "todo creates successfully !",
        "data" : todo
    }
    
@app.get("/todo")
def get_todo():
    return todos

@app.get("/todo/{todo_id}")
def get_todo_by_id(todo_id : int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message" : "todo not found !"}


# update todo
@app.put("/todo/{todo_id}")
def update_todo(todo_id : int , updated_todo : Todo):
    for index , todo in enumerate(todos): 
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message" : "todo updated successfully !",
                "data" : updated_todo
            }
    return {"message" : "todo not found !"}

# delete todo
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id : int):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message" : "todo deleted successfully !"}
    return {"message" : "todo not found !"}


# path + query + body parameter

# response model

class User(BaseModel):
    name : str
    age : int
    password : str
    
class UserResponse(BaseModel):
    name : str
    age : int
    
    
@app.get("/user" , response_model=UserResponse)
def get_user_info():
    return {
        "name" : "shivam",
        "age" : 20,
        "password" : "shiv123"
    }
    
    
# status code

@app.post("/create_user" , status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message" : "user created successfully!"
    }
 
@app.get("/create_user", status_code=status.HTTP_202_ACCEPTED)
def create_user():
    return {
        "status": "success",
        "message" : "user fetched",
        "data": {
            "name" : "shivam",
            "age" : 20,
        }
    }
    
@app.get("/users/{users_id}")
def get_user_id(users_id : int):
    if users_id != 1:
        raise HTTPException(
            status_code=404, #user not found
            detail="user not found"
        )
    return {
        "id" : 1,
        "name" : "shivam",
        "age" : 20
    }
    
# global/custom exception handling

class usernotfoundexception(Exception): #custom exception making
    def __init__(self, name: str):
        self.name = name
        
@app.get("/client/{name}")
def get_name(name :str):
    if name != "shivam":
        raise usernotfoundexception(name)
    return{
        "message": "user found",
        "name": name
    }


