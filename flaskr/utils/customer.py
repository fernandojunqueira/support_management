from ..models.models import Customer


def find_customer_by_email(email: str):
    return Customer.query.filter_by(email=email).first()


def build_response_json_customer(customer):
    return {
            'id': customer.id,
            'username': customer.username,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address
        }
