from flask import Blueprint, request

from ..utils.customer import find_customer_by_email
from ..utils.auth import check_password, generate_token


bp_login = Blueprint('login', __name__, url_prefix='/login')


@bp_login.route('/', methods=['POST'])
def session():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return {'error': 'Email or password field missing'}, 400

    customer = find_customer_by_email(email)

    if not customer:
        return {'error': 'Wrong email or password'}, 401

    if not check_password(password, customer.password):
        return {'error': 'Wrong email or password'}, 401

    payload = {"customer_id": customer.id, "email": customer.email}

    token = generate_token(payload)

    return {"token": token}, 200
