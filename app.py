from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>HEY THERE</h1>"

@app.route("/qa")
def q_and_a():
    return "q and a page"

@app.route("/login")
def login():
    return "login"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
