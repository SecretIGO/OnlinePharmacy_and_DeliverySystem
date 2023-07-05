from flask import Flask, render_template, request, redirect, url_for
from models import create_user, get_all_users

app = Flask(__name__)

@app.route('/')
def index():
    users = get_all_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    create_user(username, password, email)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)