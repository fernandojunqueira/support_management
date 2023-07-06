from ..models.models import Customer
from flask import jsonify, Blueprint, request
from ..utils.customer import find_customer_by_email, build_response_json_customer
from ..utils.auth import generate_password_hash
from ..extensions import db


bp = Blueprint('customer', __name__, url_prefix='/customer')


@bp.route('/register', methods=['POST'])
def customer_create():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    password = data.get('password')

    if not username or not email or not phone or not address or not password:
        return {"error": "Missing data"}, 400

    customer = find_customer_by_email(email)

    if customer:
        return {"error": "Email already exists"}, 409

    hashed_password = generate_password_hash(password)

    new_customer = Customer(
        username=username,
        email=email,
        phone=phone,
        address=address,
        password=hashed_password
    )
    db.session.add(new_customer)
    db.session.commit()

    customer_data = build_response_json_customer(new_customer)

    return jsonify(customer_data), 201