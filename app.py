from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
