from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/login_validation')
def login_valdiation():
    email = request.form.get('email')
    password = request.form.get('password')

    connection = sqlite3.Connect('loginData.db')
    cursor = connection.cursor()

    user = cursor.execute("SELECT * FROM USERS WHERE email=? AND password=?", (email,password)).fetchall()
    if len(user) > 0:
        return 'Welcome'
    else:
        return redirect('/')