from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import webbrowser
from threading import Timer
app = Flask(__name__)
app.secret_key = "faceiq_secret_key"

def init_db():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()
init_db()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

@app.route('/')
def home():
    return render_template("login.html")


@app.route('/register_user', methods=['POST'])
def register_user():
    fullname = request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username,email,password)
        )
        conn.commit()

    except Exception as e:
       return f"Database Error: {e}"
        
    finally:
        conn.close()

    session['user'] = username
    return redirect('/faceiq')




@app.route('/login_user', methods=['POST'])
def login_user():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    user = cur.fetchone()
    conn.close()

    if user:
        session['user'] = username
        return redirect('/faceiq')

    return "Invalid Username or Password"

@app.route('/faceiq')
def faceiq():

    if 'user' not in session:
        return redirect('/')

    return render_template("index.html")

@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)