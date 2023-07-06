from ..models.models import Ticket


def find_ticket_by_id(id):
    return Ticket.query.filter_by(id=id).first()


def build_response_dict_ticket(ticket):
    return {
        'id': ticket.id,
        'title': ticket.title,
        'description': ticket.description,
        'status': ticket.status,
        'customer': {
            "email": ticket.customer.email,
            "phone": ticket.customer.phone,
            "address": ticket.customer.address
        }
    }
