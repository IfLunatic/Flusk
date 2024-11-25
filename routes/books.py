from flask import Blueprint, request, jsonify
from models.models import db, Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.json
    title = data.get('title')
    author_id = data.get('author_id')
    publisher_id = data.get('publisher_id')
    if not title or not author_id or not publisher_id:
        return jsonify({"error": "Missing required fields"}), 400
    book = Book(title=title, author_id=author_id, publisher_id=publisher_id)
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book created", "book": {"id": book.id, "title": book.title}}), 201

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [{"id": book.id, "title": book.title, "author_id": book.author_id, "publisher_id": book.publisher_id} for book in books]
    return jsonify(result)

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    result = {"id": book.id, "title": book.title, "author_id": book.author_id, "publisher_id": book.publisher_id}
    return jsonify(result)
