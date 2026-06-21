from fastapi import FastAPI , HTTPException , Depends , Header
from jose import jwt
from datetime import datetime , timedelta , timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict
from passlib.context import CryptContext 

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DURATION = 30

# PASSWORD HASHING CONCEPT
password_context = CryptContext(schemas = ["bycrypt"])

# oauth setup
oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

# FUNCTION FOR CREATING TOKENS

def create_token(data : dict):
    todo_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=2)
    todo_encode.update(
        {
            "exp": expire    
        }
    )
    token = jwt.encode(todo_encode, SECRET_KEY , algorithm=ALGORITHM)
    return token

# login token

@app.post("/login")
def login(username: str, password: str):
    if username != "admin123" or password != "123":
        raise HTTPException(
            status_code=404,
            detail="username invalid"
        )
    token = create_token({
        "sub": username
    })
    return{
        "accessed token": token
    }
    
# token verification

def varify_token(token : str = Header(None)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        return payload
    except Exception:
        raise HTTPException(
            status_code=404,
            detail="invalid token"
        )

# protected page where use can redirect
@app.get("/secure")
def secure_get(user = Depends(varify_token)):
    return{
        "message": "secured data accessed",
        "data" : user
    }
    
    
    
        