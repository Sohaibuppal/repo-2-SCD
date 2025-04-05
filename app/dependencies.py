from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .db import SessionLocal
from . import crud, models, auth

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current user from the database
def get_current_user(db: Session = Depends(get_db), token: str = Depends(auth.oauth2_scheme)):
    user_email = auth.get_current_user(token)
    user = crud.get_user(db, email=user_email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
