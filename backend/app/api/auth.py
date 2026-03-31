from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core import security
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import Token, RefreshRequest
from app.db.session import get_db
from app.models.user import User
from app.models.session import UserSession
from app.core.config import settings
import datetime

router = APIRouter()

@router.post("/register", response_model=dict)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if not user_in.password or not user_in.password.strip():
        raise HTTPException(status_code=400, detail="Password cannot be empty")
    
    user = db.query(User).filter(User.email == user_in.email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = User(
        email=user_in.email,
        password_hash=security.get_password_hash(user_in.password),
        preferred_language=user_in.preferred_language,
        preferred_era=user_in.preferred_era
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully"}

@router.post("/login", response_model=dict)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    if not user_in.password or not user_in.password.strip():
        raise HTTPException(status_code=400, detail="Password cannot be empty")
    
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user or not security.verify_password(user_in.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
    refresh_token = security.create_refresh_token(user.id)
    
    db_session = UserSession(
        user_id=user.id,
        refresh_token=refresh_token,
        expires_at=datetime.datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    db.add(db_session)
    db.commit()
    
    return {
        "access_token": access_token, 
        "refresh_token": refresh_token, 
        "user": {"id": user.id, "email": user.email}
    }
