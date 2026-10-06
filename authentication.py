from datetime import  datetime,timedelta
from jose import jwt
from pwdlib import PasswordHash
from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

import os
from dotenv import load_dotenv

load_dotenv()
SECURITY_KEY=os.environ.get("SECURITY_KEY")
ALGORITHM="HS256"
EXPIRE_MINUTES=30

password_context=PasswordHash.recommended()

security=HTTPBearer()

def hash_password(password:str):
    return password_context.hash(password)

def password_verify(password:str,hash_pwd:str):
    return password_context.verify(password,hash_pwd)

def create_token(username:str):
    expire=datetime.utcnow()+timedelta(EXPIRE_MINUTES)

    data={
        "Subject":username,
        "Expire":int(expire.timestamp())
    }

    token=jwt.encode(data,SECURITY_KEY,ALGORITHM)

    return token

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)):
    token=credentials.credentials
    try:
        playload=jwt.decode(token,SECURITY_KEY,ALGORITHM)

        username=playload.get("Subject")

        if username is None:
            raise HTTPException(status_code=401,detail="Invalid token")

        return username
    except Exception:
        raise HTTPException(status_code=401,detail="Invalid expired or token")
