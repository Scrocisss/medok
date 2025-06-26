from flask import Flask, render_template, request, redirect, make_response
import jwt, os, sqlite3
from db import init_db, get_user, create_user
from utils import generate_password, generate_secret_key
from datetime import datetime, timedelta

app = Flask(__name__, static_url_path='/static')
SECRET_KEY = generate_secret_key()
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", generate_password())

init_db()

if not get_user("admin"):
    create_user("admin", ADMIN_PASSWORD, is_admin=True)
    print(f"[INFO] Admin password: {ADMIN_PASSWORD}")

def generate_token(username, role):
    payload = {
        'username': username,
        'role': role,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256', 'none'], options={"verify_signature": False})

@app.route('/')
def index():
    token = request.cookies.get('token')
    if not token:
        return redirect('/login')
    try:
        payload = decode_token(token)
        return render_template('index.html', username=payload['username'], role=payload['role'])
    except:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        user = get_user(u)
        if user and user['password'] == p:
            token = generate_token(u, user['role'])
            resp = make_response(redirect('/'))
            resp.set_cookie('token', token)
            return resp
        error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        if get_user(u):
            error = "User already exists"
        else:
            create_user(u, p)
            return redirect('/login')
    return render_template('register.html', error=error)

@app.route('/admin')
def admin():
    token = request.cookies.get('token')
    try:
        data = decode_token(token)
        if data['role'] != 'admin':
            return render_template('admin.html', flag='CODEBY{F4K3_FL4G}')
        return render_template('admin.html', flag="CODEBY{R3D4C73D}")
    except Exception:
        return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
