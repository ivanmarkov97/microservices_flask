import json

from flask import Flask

from src.profile import get_main_info, get_additional_info


app = Flask(__name__)
app.config['DB_CONFIG'] = json.load(open('configs/db.json'))

app.add_url_rule('/main-info/<user_id>', view_func=get_main_info, methods=['GET'])
app.add_url_rule('/additional-info/<user_id>', view_func=get_additional_info, methods=['GET'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
