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
