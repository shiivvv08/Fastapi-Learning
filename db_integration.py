from fastapi import FastAPI , HTTPException 
import uvicorn
import sqlite3


app = FastAPI()

conn = sqlite3.connect("test.db",check_same_thread=False)
Cursor = conn.cursor() # ye sql query ko run krega cursor

Cursor.execute("""
               
CREATE TABLE IF NOT EXISTS todos(
    id int primary key,
    title text,
    completed text 
)             

        """)

conn.commit()

@app.get("/")
def get_home():
    return {
        "message": "sqlite connected successfully"
    }
    


