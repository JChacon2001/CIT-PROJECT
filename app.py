from flask import Flask, render_template
from routes import html_bp
from db import db
from flask_wtf import FlaskForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'

app.register_blueprint(html_bp, url_prefix="/")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    with app.app_context():
        db.create_all()