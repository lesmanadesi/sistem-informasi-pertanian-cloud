from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ======================
# HALAMAN LOGIN (GET)
# ======================
@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

# ======================
# PROSES LOGIN (POST)
# ======================
@app.route("/login", methods=["POST"])
def login():
    # nanti bisa tambah cek username/password
    return redirect(url_for("dashboard"))

# ======================
# DASHBOARD
# ======================
@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
