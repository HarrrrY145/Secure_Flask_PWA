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
        return redirect(f'/home?fname={user[0][0]}&email={user[0][1]}&email={user[0][2]}')
    else:
        return redirect('/')
@app.route('/home')
def home():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')

    return render_template('home.html', fname=fname, lname=lname, email=email)