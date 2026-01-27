from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# =========================
# ROUTE HOME / LOGIN
# =========================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # login sederhana (contoh)
        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Username atau password salah")

    return render_template("login.html")


# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# =========================
# TAMBAH LAHAN
# =========================
@app.route("/tambah-lahan", methods=["GET", "POST"])
def tambah_lahan():
    if request.method == "POST":
        # contoh ambil data form
        nama_lahan = request.form.get("nama_lahan")
        luas = request.form.get("luas")

        # nanti bisa disimpan ke database
        return redirect(url_for("dashboard"))

    return render_template("tambah_lahan.html")


# =========================
# RUN APP (WAJIB UNTUK RAILWAY)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
