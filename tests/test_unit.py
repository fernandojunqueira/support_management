from flaskr.utils.auth import (
    generate_password_hash, check_password, generate_token
)
from flaskr.utils.customer import (
    find_customer_by_email, find_customer_by_id, build_response_dict_customer
)

customer_dict = {}


def test_before_all(client):
    response = client.post('/customer/register', json={
	    "username": "john",
        "email": "john@mail.com",
        "phone": "48999999999",
        "address": "address",
        "password": "1234"
    })

    customer_dict.update({"id": response.json['id']})
    customer_dict.update({"email": response.json['email']})

    assert response.status_code == 201


def test_find_customer_by_email():
    response = find_customer_by_email('john@mail.com')

    assert response.id == customer_dict['id']


def test_find_customer_by_id():
    response = find_customer_by_id(customer_dict['id'])

    assert response.email == customer_dict['email']


def test_generate_password_hash():
    hashed_password = generate_password_hash('1234')
    customer_dict.update({"hashed_password": hashed_password})

    assert len(hashed_password) == 60


def test_if_check_password_returns_true():
    response = check_password('1234', customer_dict["hashed_password"])

    assert response is True


def test_if_function_generate_token_return_str_len_137():
    response = generate_token({"customer_id": -1, "email": "john@mail.com"})

    assert len(response) == 137


def test_build_response_dict_customer():
    customer = find_customer_by_id(customer_dict['id'])
    response = build_response_dict_customer(customer)

    assert type(response) == dict


def test_after_all(client):
    client.delete(f'customer/{customer_dict["id"]}')
    del customer_dict["id"]
    del customer_dict["email"]
    del customer_dict["hashed_password"]
