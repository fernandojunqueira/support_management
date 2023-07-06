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


def get_id_from_token(bearer_token: str):

    try:

        token = bearer_token.split(' ')[1]

        payload = jwt.decode(
                token, algorithms=['HS256'],
                options={'verify_signature': False}
                )

        return payload.get('customer_id')
    except jwt.exceptions.InvalidTokenError:
        return 'Invalid'
