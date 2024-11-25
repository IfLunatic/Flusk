from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', cascade="all, delete-orphan", lazy=True)

class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='publisher', cascade="all, delete-orphan", lazy=True)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
