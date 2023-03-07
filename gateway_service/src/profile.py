import json

import requests
from flask import request


AUTH_SERVICE_URL = 'http://127.0.0.1:5002'
PROFILE_SERVICE_URL = 'http://127.0.0.1:5003'


def collect_profile_data():
    user_token = request.args.get('token', '')
    user_id = requests.get(f'{AUTH_SERVICE_URL}/token/user-id?token={user_token}')
    main_profile_info = requests.get(f'{PROFILE_SERVICE_URL}/main-info/{user_id}')
    additional_profile_info = requests.get(f'{PROFILE_SERVICE_URL}/additional-info/{user_id}')
    return json.dumps(
        {
            'main': main_profile_info,
            'additional': additional_profile_info
        }
    )
