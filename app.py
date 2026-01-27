from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ======================
# LOGIN
# ======================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Username atau password salah")

    return render_template("login.html")


# ======================
# DASHBOARD
# ======================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ======================
# TAMBAH LAHAN
# ======================
@app.route("/tambah-lahan")
def tambah_lahan():
    return render_template("tambah_lahan.html")


# ======================
# RUN (WAJIB UNTUK RAILWAY)
# ======================
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
