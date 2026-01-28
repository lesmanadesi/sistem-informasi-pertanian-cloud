from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

app = Flask(__name__)
app.secret_key = 'secretkey123'  # bebas, asal ada

# ===============================
# KONFIGURASI DATABASE
# ===============================
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'pertanian')

mysql = MySQL(app)

# ===============================
# ROUTE HALAMAN UTAMA (GET)
# ===============================
@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

# ===============================
# ROUTE LOGIN (GET + POST)
# ===============================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE username=%s AND password=%s',
            (username, password)
        )
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['username'] = account['username']
            return redirect(url_for('dashboard'))
        else:
            return 'Login gagal'

    # kalau GET
    return render_template('login.html')

# ===============================
# DASHBOARD
# ===============================
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

# ===============================
# LOGOUT
# ===============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ===============================
# RUN APP (LOCAL + RAILWAY)
# ===============================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
