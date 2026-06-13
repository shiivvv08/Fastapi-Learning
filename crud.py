from fastapi import FastAPI
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

