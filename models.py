from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)  
    author = db.Column(db.String(100), nullable=False, index=True)  
    publisher = db.Column(db.String(100), nullable=False, index=False) 
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"
