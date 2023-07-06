from flaskr.utils.auth import (
    generate_password_hash,
)

def test_generate_password_hash():
    hashed_password = generate_password_hash('1234')
    
    assert len(hashed_password) == 60