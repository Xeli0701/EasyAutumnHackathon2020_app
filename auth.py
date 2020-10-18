import hashlib
import db
from models import User
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi import HTTPException

def auth(credentials):
    """
    Basic認証を行う関数
    sqlite3のuserとpasswordを照合する
    """
    # Basic Auth info
    username = credentials.username
    password = hashlib.md5(credentials.password.encode()).hexdigest()

    # get user from db
    user = db.session.query(User).filter(User.username == username).first()
    db.session.close()

    # if user isn't exist  or  password incorrect
    if user is None or user.password != password:
        error = 'Incorrect username or password'
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Basic"},
        )
    return username