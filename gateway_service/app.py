from flask import Flask

from src.profile import collect_profile_data
from src.auth import auth_user


app = Flask(__name__)

app.add_url_rule('/profile', view_func=collect_profile_data)
app.add_url_rule('/auth', view_func=auth_user, methods=['POST'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
