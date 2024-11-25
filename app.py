from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models.models import db
from routes.books import books_bp


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


app.register_blueprint(books_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
