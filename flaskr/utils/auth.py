from passlib.hash import bcrypt
import jwt
import os
from dotenv import load_dotenv
load_dotenv()


def generate_password_hash(password: str):
    return bcrypt.hash(password)


def check_password(password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)


def generate_token(payload: dict):
    SECRET_KEY = os.getenv("SECRET_KEY")

    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
