from flask import Flask
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "APP HIDUP - ROOT OK"

# JANGAN hapus ini (aman untuk local & prod)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

