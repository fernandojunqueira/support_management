from passlib.hash import bcrypt


def generate_password_hash(password: str):
    return bcrypt.hash(password)