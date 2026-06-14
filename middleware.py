from fastapi import FastAPI , status , HTTPException , Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse 
import uvicorn , time 

# ek function jo request or response ke beech me hota h use middleware kehte h

app = FastAPI()


""" @app.middleware("http")
async def my_middleware(request : Request , call_next):
    print("request recieved")
    response = await call_next(request) 
    print("response send")
    return response """
    
@app.middleware("http")
async def log_middleware(request : Request , call_next):
    start_time = time.time()
    print("request recieved")
    response = await call_next(request)
    print("response send")
    process_time = time.time() - start_time
    print(f"path: {request.url.path} | time: {process_time}")
    return response

 



