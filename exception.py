from fastapi import FastAPI , status , HTTPException , Request , Header
from pydantic import BaseModel
import uvicorn
from fastapi import Depends
# for global exception we import some modules
from fastapi.responses import JSONResponse

app = FastAPI()

# global or custom error handling 

class usernotfounderror(Exception):
    def __init__(self , name : str):
        self.name = name
        
@app.get("/clients/{name}")
def get_client(name : str):
    if name != "shivam":
        raise usernotfounderror(name)
    return {
        "message": "user found successfully",
        "name": name
    }
    
# global exception

@app.exception_handler(usernotfounderror)
def user_not_found(request : Request , exc : usernotfounderror):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error : user not found",
            "message" : f"user {exc.name} not found"
        }
    )
    
# dependancy injection = a logic which is required for another function 

def common_logic():
    return {
        "message": "common logic executed"
    }
    
@app.get("/home")
def get_home(data = Depends(common_logic)):
    return {
        "data" : data
    }
    
def verify_token(token : str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code= 401,
            detail= "user unauthorized"
        )
    return {
        "message": "user authorized successfuly",
        
    }
    
@app.get("/secure-data/")
def get_user(user = Depends(verify_token)):
    return {
        "message": "seure data accessed",
        "user": user
    }
    
    
    
    
    
