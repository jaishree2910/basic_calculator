from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']

        conn = sqlite3.connect('emails.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(email) VALUES(?)",
            (email,)
        )

        conn.commit()
        conn.close()

        return "Email Stored Successfully!"

    return render_template('index.html')

@app.route('/emails')
def show_emails():
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    emails = cursor.fetchall()

    conn.close()

    return str(emails)

if __name__ == '__main__':
    app.run(debug=True)