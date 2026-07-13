from flask import Flask, request
from automation import start

app = Flask(__name__)
ai = start()

@app.route("/api", methods=["GET"])
def home():
    q = request.args.get("q", "")
    return ai(q)

if __name__ == "__main__":
    app.run(port=3000)