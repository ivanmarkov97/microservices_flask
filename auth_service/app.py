import json

from flask import Flask

from src.auth import get_user, create_token_for_user, get_user_id_by_token


app = Flask(__name__)
app.config['DB_CONFIG'] = json.load(open('configs/db.json'))

app.add_url_rule('/user', view_func=get_user, methods=['GET'])
app.add_url_rule('/token', view_func=create_token_for_user, methods=['POST'])
app.add_url_rule('/token/user-id', view_func=get_user_id_by_token, methods=['GET'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
