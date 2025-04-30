from flask import Flask
from routes import html_bp
app = Flask(__name__)


app.register_blueprint(html_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
