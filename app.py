from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash
import config

app = Flask(__name__)
app.secret_key = 'pertanian_secret'

# KONFIG MYSQL
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB

mysql = MySQL(app)

# ================= LOGIN =================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()

        if user and check_password_hash(user[2], password):
            session['login'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))

        return "Login gagal"

    return render_template('login.html')

# ================= DASHBOARD =================
@app.route('/dashboard')
def dashboard():
    if 'login' not in session:
        return redirect('/')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM lahan")
    lahan = cur.fetchall()

    return render_template('dashboard.html', lahan=lahan)

# ================= TAMBAH LAHAN =================
@app.route('/tambah_lahan', methods=['GET', 'POST'])
def tambah_lahan():
    if 'login' not in session:
        return redirect('/')

    if request.method == 'POST':
        nama = request.form['nama_lahan']
        luas = request.form['luas']
        lokasi = request.form['lokasi']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO lahan (nama_lahan, luas, lokasi) VALUES (%s,%s,%s)",
            (nama, luas, lokasi)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/dashboard')

    return render_template('tambah_lahan.html')

# ================= LOGOUT =================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
