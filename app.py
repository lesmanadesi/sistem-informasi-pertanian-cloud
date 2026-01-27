from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/masuk")
def masuk():
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
