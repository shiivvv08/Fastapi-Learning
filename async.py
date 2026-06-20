from fastapi import FastAPI
import time , asyncio
import uvicorn

app = FastAPI()

@app.get("/home")
async def home():
    await asyncio.sleep(3)
    return {
        "message": "Done"
    }
    
