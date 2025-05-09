from flask import Flask, render_template
from routes import html_bp
from db import db


def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   
    db.init_app(app)

  
    app.register_blueprint(html_bp, url_prefix='/')

   
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

 
    with app.app_context():
        db.create_all()

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)