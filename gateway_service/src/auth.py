import json

import requests
from flask import request


AUTH_SERVICE_URL = 'http://127.0.0.1:5002'


def auth_user():
    request_body = request.json
    request_login = request_body.get('login', '')
    request_password = request_body.get('password', '')
    user = requests.get(f'{AUTH_SERVICE_URL}/user?login={request_login}&password={request_password}').json()
    if user:
        token = requests.post(f'{AUTH_SERVICE_URL}/token', data=user)
        return json.dumps({'token': token})
    return json.dumps({})
