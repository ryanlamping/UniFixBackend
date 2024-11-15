from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext
from datetime import date

from schemas.user import UserCreate


# password hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# function to hash password
def get_password_hash(password):
    return pwd_context.hash(password)

def user_sign_up(db: Session, user_create: UserCreate):
    # hasing password
    hashed_password = get_password_hash(user_create.password)
    
    # creating user
    new_user = User(
        name = user_create.name,
        password = hashed_password,
        email = user_create.email,
        roleid = user_create.roleid,
        addressid = user_create.addressid,
        phonenumber = user_create.phonenumber
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Create token and successfully login here
    
    return new_user

# read user with input of email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()