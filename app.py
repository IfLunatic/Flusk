from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from routes.books import books_bp
from routes.auth import auth_bp
from models.models import db, Book 
import time

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.drop_all()
    db.create_all()  


def measure_query_time(query_func, *args, **kwargs):
    """Функція для вимірювання часу виконання запиту"""
    start_time = time.time()
    query_func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


def test_insert(n):
    """Тестуємо вставку записів в базу даних"""
    books = [Book(title=f"Book {i}", author=f"Author {i}", publisher=f"Publisher {i}") for i in range(n)]
    db.session.bulk_save_objects(books)
    db.session.commit()


def test_select():
    """Тестуємо вибірку всіх записів з таблиці книг"""
    return Book.query.filter_by(author="Author 1").all()  


def test_update():
    """Тестуємо оновлення записів"""
    book = Book.query.filter_by(author="Author 1").first()
    if book:
        book.title = "Updated Title"
        db.session.commit()


def test_delete():
    """Тестуємо видалення записів"""
    book = Book.query.filter_by(author="Author 1").first()
    if book:
        db.session.delete(book)
        db.session.commit()


def benchmark_operations():
    """Виконуємо заміри для кожної операції з різною кількістю записів"""
    results = {}

    for n in [1000, 10000, 100000, 1000000]:
        print(f"Running tests with {n} records...")

        insert_time = measure_query_time(test_insert, n)
        results[f"Insert {n}"] = insert_time

        select_time = measure_query_time(test_select)
        results[f"Select {n}"] = select_time

        update_time = measure_query_time(test_update)
        results[f"Update {n}"] = update_time

        delete_time = measure_query_time(test_delete)
        results[f"Delete {n}"] = delete_time

    return results


def print_benchmark_results(results):
    print("\nBenchmark Results:")
    for operation, time_taken in results.items():
        print(f"{operation}: {time_taken:.5f} seconds")



with app.app_context():
    benchmark_results = benchmark_operations()
    print_benchmark_results(benchmark_results)


app.register_blueprint(books_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
