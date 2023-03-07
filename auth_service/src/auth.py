import base64
import json

from flask import request, current_app, make_response

from src.database import DBConnector


def get_user():
    credentials = request.args
    login = credentials.get('login', None)
    password = credentials.get('password', None)

    db_config = current_app.config['DB_CONFIG']
    db = DBConnector(db_config)

    user = db.get_user(login=login, password=password)

    if user:
        response = make_response(user.to_dict(), 200)
    else:
        response = make_response({}, 204)
    return response


def create_token_for_user():
    user_data = request.json
    user_string = f'{user_data["login"]}:{user_data["name"]}:auth-service'

    message_bytes = user_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    return base64_message


def validate_token_for_user():
    token = request.args.get('token', '')

    base64_bytes = token.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    user_string = message_bytes.decode('ascii')

    user_string_parts = user_string.split(':')
    is_valid = True

    if len(user_string_parts) != 3:
        is_valid = False
    if user_string_parts[-1] != 'auth-service':
        is_valid = False

    return json.dumps({'is_valid': is_valid})


def get_user_id_by_token():
    _ = request.args.get('token', '')
    return str(123)  # constant for simplicity
