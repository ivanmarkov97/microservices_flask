import json

import requests

from flask import Flask, render_template, session, redirect, request


app = Flask(__name__)
app.secret_key = 'secret session key'

API_GATEWAY_ADDRESS = '127.0.0.1:5001'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    token = session.get('token', '')
    profile_info = requests.get(f'{API_GATEWAY_ADDRESS}/profile?token={token}')
    if profile_info:
        return render_template('profile.html', content=profile_info)
    else:
        return redirect('/auth')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        return render_template('auth.html')
    else:
        user_data = json.dumps({
            'login': request.form.get('login', ''),
            'password': request.form.get('password', '')
        })
        user_credentials = requests.post(f'{API_GATEWAY_ADDRESS}/auth', data=user_data).json()
        if user_credentials:
            session['token'] = user_credentials['token']
        else:
            return render_template('auth.html', message='Invalid login or password')
        return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
