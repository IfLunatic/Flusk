from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from routes.books import books_bp
from routes.auth import auth_bp
from models.models import db


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)


jwt = JWTManager(app)

with app.app_context():
    db.drop_all()  
    db.create_all() 


# Реєстрація Blueprint'ів
app.register_blueprint(books_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
