from fastapi import FastAPI , requests , Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# limiter setup

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# error handling

@app.exception_handler(RateLimitExceeded)
def rate_limit_exceed(request: Request , exc: RateLimitExceeded):
    
    return JSONResponse(
        status_code=429,
        content={
            "detail" : "too many requests"
        }
    )
    
# rate limiter api
@app.get("/home")
@limiter.limit("5/minute")
def get_data(request: Request):
    return {
        "message": "success"
    }
    
    
    
    