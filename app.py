from flask import Flask, render_template
from routes import html_bp
app = Flask(__name__)


app.register_blueprint(html_bp, url_prefix="/")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
