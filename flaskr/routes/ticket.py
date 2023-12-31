from ..models.models import Ticket
from flask import Blueprint, request, jsonify
from ..utils.ticket import build_response_dict_ticket, find_ticket_by_id
from ..utils.auth import get_id_from_token
from ..utils.customer import find_customer_by_id

from ..extensions import db

bp_ticket = Blueprint('ticket', __name__, url_prefix='/ticket')


@bp_ticket.route('/<int:customer_id>', methods=['POST'])
def ticket_create(customer_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')
    customer_id = customer_id

    bearer_token = request.headers.get('Authorization')

    if not description:
        return {"error": "Description field is missing"}

    if not bearer_token:
        return {'error': 'Missing token'}, 401

    customer_id_payload = get_id_from_token(bearer_token)

    if customer_id_payload == 'Invalid':
        return {'error': 'Invalid token'}, 401

    if customer_id_payload != customer_id:
        return {"error": "You need to be the owner to access this route."}, 403

    customer = find_customer_by_id(customer_id)

    if not customer:
        return {'error': 'Customer not found'}, 404

    ticket = Ticket(
        title=title,
        description=description,
        status=status,
        customer_id=customer_id
    )

    db.session.add(ticket)
    db.session.commit()

    ticket_data = build_response_dict_ticket(ticket)

    return jsonify(ticket_data), 201


@bp_ticket.route('/<int:ticket_id>', methods=['PATCH', 'DELETE'])
def ticket_update_or_delete(ticket_id):
    if request.method == 'PATCH':

        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        status = data.get('status')

        bearer_token = request.headers.get('Authorization')

        if not bearer_token:
            return {'error': 'Missing token'}, 401

        customer_id_payload = get_id_from_token(bearer_token)

        if customer_id_payload == 'Invalid':
            return {'error': 'Invalid token'}, 401

        ticket = find_ticket_by_id(ticket_id)

        if not ticket:
            return {"error": "Ticket not found"}, 404

        if title:
            ticket.title = title

        if description:
            ticket.description = description

        if status:
            ticket.status = status

        db.session.commit()

        ticket_data = build_response_dict_ticket(ticket)

        return jsonify(ticket_data), 200
    else:
        bearer_token = request.headers.get('Authorization')

        if not bearer_token:
            return {'error': 'Missing token'}, 401

        customer_id_payload = get_id_from_token(bearer_token)

        if customer_id_payload == 'Invalid':
            return {'error': 'Invalid token'}, 401

        ticket = find_ticket_by_id(ticket_id)

        if not ticket:
            return {"error": "Ticket not found"}, 404

        db.session.delete(ticket)
        db.session.commit()

        return {"msg": "Deleted"}, 204


@bp_ticket.route('/', methods=['GET'])
def ticket_list():

    bearer_token = request.headers.get('Authorization')

    if not bearer_token:
        return {'error': 'Missing token'}, 401

    customer_id_payload = get_id_from_token(bearer_token)

    if customer_id_payload == 'Invalid':
        return {'error': 'Invalid token'}, 401

    tickets = Ticket.query.all()

    ticket_list = []

    for ticket in tickets:
        ticket_data = build_response_dict_ticket(ticket)
        ticket_list.append(ticket_data)

    return jsonify(ticket_list), 200
