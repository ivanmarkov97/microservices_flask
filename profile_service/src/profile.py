import json

from flask import current_app

from src.database import DBConnector


def get_main_info(user_id: str):
    db_config = current_app.config['DB_CONFIG']
    db = DBConnector(db_config)

    user_info = db.get_user_main_info(user_id=user_id)

    if user_info:
        response = json.dumps(user_info.to_dict())
    else:
        response = json.dumps({})
    return response


def get_additional_info(user_id: str):
    db_config = current_app.config['DB_CONFIG']
    db = DBConnector(db_config)

    user_add_info = db.get_user_additional_info(user_id=user_id)

    if user_add_info:
        response = json.dumps(user_add_info.to_dict())
    else:
        response = json.dumps({})
    return response
