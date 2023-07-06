from ..models.models import Customer


def find_customer_by_email(email: str):
    return Customer.query.filter_by(email=email).first()


def find_customer_by_id(id: int):
    return Customer.query.filter_by(id=id).first()


def build_response_dict_customer(customer):
    return {
            'id': customer.id,
            'username': customer.username,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        }
