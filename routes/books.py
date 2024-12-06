from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.models import db, Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
@jwt_required()  
def create_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')  
    publisher = data.get('publisher')  
    
    if not title or not author or not publisher:
        return jsonify({"error": "Missing required fields"}), 400
    
    book = Book(title=title, author=author, publisher=publisher)
    db.session.add(book)
    db.session.commit()
    
    return jsonify({"message": "Book created", "book": {"id": book.id, "title": book.title}}), 201

@books_bp.route('/books', methods=['GET'])
@jwt_required()  
def get_books():
    books = Book.query.all()
    result = [{"id": book.id, "title": book.title, "author": book.author, "publisher": book.publisher} for book in books]
    return jsonify(result)

@books_bp.route('/books/<int:book_id>', methods=['GET'])
@jwt_required()  
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    result = {"id": book.id, "title": book.title, "author": book.author, "publisher": book.publisher}
    return jsonify(result)
