from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/tambah_lahan")
def tambah_lahan():
    return render_template("tambah_lahan.html")

if __name__ == "__main__":
    app.run()

